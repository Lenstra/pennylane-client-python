"""Tests for PennylaneClient.paginate / fetch_all (no network)."""

import asyncio

from pennylane_client import PennylaneClient


def _page(ids, next_cursor=None) -> dict:
    return {
        "items": [{"id": i} for i in ids],
        "has_more": next_cursor is not None,
        "next_cursor": next_cursor,
    }


def make_operation(pages: list[dict]):
    """Fake list operation returning ``pages`` in order and logging its kwargs."""
    calls: list[dict] = []
    page_iter = iter(pages)

    async def operation(*args, **kwargs):
        calls.append({"args": args, **kwargs})
        return next(page_iter)

    return operation, calls


def collect(operation, *args, **kwargs) -> list:
    client = PennylaneClient("t")

    async def _run():
        return [item async for item in client.paginate(operation, *args, **kwargs)]

    return asyncio.run(_run())


def test_single_page():
    operation, calls = make_operation([_page([1, 2])])
    assert collect(operation) == [{"id": 1}, {"id": 2}]
    assert calls == [{"args": (), "cursor": None, "limit": 100}]


def test_follows_next_cursor():
    operation, calls = make_operation(
        [_page([1, 2], "c1"), _page([3], "c2"), _page([4])]
    )
    assert [item["id"] for item in collect(operation)] == [1, 2, 3, 4]
    assert [c["cursor"] for c in calls] == [None, "c1", "c2"]


def test_forwards_args_and_kwargs():
    operation, calls = make_operation([_page([1])])
    collect(
        operation, "7", limit=20, filter=[{"field": "id", "operator": "eq", "value": 1}]
    )
    assert calls[0]["args"] == ("7",)
    assert calls[0]["limit"] == 20
    assert calls[0]["filter"][0]["field"] == "id"


def test_stops_without_next_cursor():
    operation, calls = make_operation(
        [{"items": [{"id": 1}], "has_more": True, "next_cursor": None}]
    )
    assert collect(operation) == [{"id": 1}]
    assert len(calls) == 1


def test_fetch_all():
    operation, _ = make_operation([_page([1], "c1"), _page([2])])
    client = PennylaneClient("t")
    assert asyncio.run(client.fetch_all(operation)) == [{"id": 1}, {"id": 2}]
