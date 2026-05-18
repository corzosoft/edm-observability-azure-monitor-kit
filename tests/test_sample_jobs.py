from io import StringIO

from edm_observability.correlation import set_correlation_id
from edm_observability.logger import JsonLogger
from edm_observability.sample_file_ingestion_job import run_file_ingestion_job
from edm_observability.sample_reconciliation_job import (
    run_data_quality_validation_job,
    run_reconciliation_job,
)
from edm_observability.telemetry_client import TelemetryClient


def test_file_ingestion_job_logs_failure_with_correlation_id() -> None:
    stream = StringIO()
    telemetry = TelemetryClient()
    set_correlation_id("33333333-3333-3333-3333-333333333333")

    result = run_file_ingestion_job(
        expected_file_arrived=False,
        logger=JsonLogger(stream),
        telemetry=telemetry,
    )

    assert result.job_status == "FAILED"
    assert result.error_message
    assert "33333333-3333-3333-3333-333333333333" in stream.getvalue()
    assert telemetry.emitted_events[0]["name"] == "edm_job_completed"


def test_reconciliation_and_data_quality_jobs_succeed() -> None:
    set_correlation_id("44444444-4444-4444-4444-444444444444")
    logger = JsonLogger(StringIO())

    dq_result = run_data_quality_validation_job(logger=logger)
    reconciliation_result = run_reconciliation_job(logger=logger)

    assert dq_result.validation_failure_count == 3
    assert reconciliation_result.job_status == "SUCCEEDED"
