from __future__ import annotations

from contextvars import ContextVar
from secrets import token_hex
from uuid import UUID, uuid4

_correlation_id: ContextVar[str | None] = ContextVar("correlation_id", default=None)
_trace_id: ContextVar[str | None] = ContextVar("trace_id", default=None)
_span_id: ContextVar[str | None] = ContextVar("span_id", default=None)


def new_correlation_id() -> str:
    correlation_id = str(uuid4())
    _correlation_id.set(correlation_id)
    _trace_id.set(correlation_id.replace("-", ""))
    _span_id.set(token_hex(8))
    return correlation_id


def set_correlation_id(correlation_id: str) -> str:
    UUID(correlation_id)
    _correlation_id.set(correlation_id)
    _trace_id.set(correlation_id.replace("-", ""))
    _span_id.set(token_hex(8))
    return correlation_id


def get_correlation_id() -> str:
    existing = _correlation_id.get()
    if existing:
        return existing
    return new_correlation_id()


def get_traceparent() -> str:
    get_correlation_id()
    trace_id = _trace_id.get() or token_hex(16)
    span_id = _span_id.get() or token_hex(8)
    return f"00-{trace_id}-{span_id}-01"
