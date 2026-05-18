import json
from io import StringIO

from edm_observability.correlation import set_correlation_id
from edm_observability.logger import JsonLogger


def test_json_logger_writes_structured_event() -> None:
    stream = StringIO()
    set_correlation_id("22222222-2222-2222-2222-222222222222")

    event = JsonLogger(stream).info("job_completed", job_name="file_ingestion", record_count=10)
    line = json.loads(stream.getvalue())

    assert event["correlation_id"] == "22222222-2222-2222-2222-222222222222"
    assert line["event_name"] == "job_completed"
    assert line["record_count"] == 10
    assert line["level"] == "INFO"
    assert line["traceparent"].startswith("00-")
