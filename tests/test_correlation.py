from uuid import UUID

import pytest

from edm_observability.correlation import (
    get_correlation_id,
    get_traceparent,
    new_correlation_id,
    set_correlation_id,
)


def test_new_correlation_id_is_valid_uuid() -> None:
    correlation_id = new_correlation_id()

    assert str(UUID(correlation_id)) == correlation_id
    assert get_correlation_id() == correlation_id


def test_set_correlation_id_validates_uuid() -> None:
    correlation_id = "11111111-1111-1111-1111-111111111111"

    assert set_correlation_id(correlation_id) == correlation_id
    with pytest.raises(ValueError):
        set_correlation_id("not-a-uuid")


def test_traceparent_uses_correlation_id_as_trace_id() -> None:
    correlation_id = "55555555-5555-5555-5555-555555555555"
    set_correlation_id(correlation_id)

    traceparent = get_traceparent()

    assert traceparent.startswith("00-55555555555555555555555555555555-")
    assert traceparent.endswith("-01")
