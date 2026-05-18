from __future__ import annotations

from time import perf_counter

from edm_observability.correlation import get_correlation_id
from edm_observability.logger import JsonLogger
from edm_observability.sample_file_ingestion_job import JobResult
from edm_observability.telemetry_client import TelemetryClient


def run_data_quality_validation_job(
    source_system: str = "SYNTH_VENDOR_A",
    record_count: int = 100,
    validation_failure_count: int = 3,
    logger: JsonLogger | None = None,
    telemetry: TelemetryClient | None = None,
) -> JobResult:
    return _run_job(
        job_name="data_quality_validation",
        source_system=source_system,
        record_count=record_count,
        validation_failure_count=validation_failure_count,
        fail=False,
        logger=logger,
        telemetry=telemetry,
    )


def run_reconciliation_job(
    source_system: str = "GOLDEN_SOURCE",
    record_count: int = 97,
    validation_failure_count: int = 0,
    fail: bool = False,
    logger: JsonLogger | None = None,
    telemetry: TelemetryClient | None = None,
) -> JobResult:
    return _run_job(
        job_name="reconciliation",
        source_system=source_system,
        record_count=record_count,
        validation_failure_count=validation_failure_count,
        fail=fail,
        logger=logger,
        telemetry=telemetry,
    )


def _run_job(
    job_name: str,
    source_system: str,
    record_count: int,
    validation_failure_count: int,
    fail: bool,
    logger: JsonLogger | None,
    telemetry: TelemetryClient | None,
) -> JobResult:
    log = logger or JsonLogger()
    telemetry_client = telemetry or TelemetryClient()
    correlation_id = get_correlation_id()
    started = perf_counter()
    log.info("job_started", job_name=job_name, source_system=source_system)
    status = "FAILED" if fail else "SUCCEEDED"
    error = "Synthetic reconciliation failure" if fail else ""
    result = JobResult(
        job_name,
        status,
        correlation_id,
        source_system,
        record_count,
        validation_failure_count,
        (perf_counter() - started) * 1000,
        error,
    )
    fields = result.__dict__
    if fail:
        log.error("job_completed", **fields)
    else:
        log.info("job_completed", **fields)
    telemetry_client.track_event("edm_job_completed", fields)
    return result
