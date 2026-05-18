from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter

from edm_observability.correlation import get_correlation_id
from edm_observability.logger import JsonLogger
from edm_observability.telemetry_client import TelemetryClient


@dataclass(frozen=True)
class JobResult:
    job_name: str
    job_status: str
    correlation_id: str
    source_system: str
    record_count: int
    validation_failure_count: int
    duration_ms: float
    error_message: str = ""


def run_file_ingestion_job(
    source_system: str = "SYNTH_VENDOR_A",
    record_count: int = 100,
    expected_file_arrived: bool = True,
    logger: JsonLogger | None = None,
    telemetry: TelemetryClient | None = None,
) -> JobResult:
    log = logger or JsonLogger()
    telemetry_client = telemetry or TelemetryClient()
    correlation_id = get_correlation_id()
    started = perf_counter()
    log.info("job_started", job_name="file_ingestion", source_system=source_system)

    status = "SUCCEEDED" if expected_file_arrived else "FAILED"
    error = "" if expected_file_arrived else "Expected source file did not arrive"
    duration_ms = (perf_counter() - started) * 1000
    result = JobResult(
        "file_ingestion",
        status,
        correlation_id,
        source_system,
        record_count if expected_file_arrived else 0,
        0,
        duration_ms,
        error,
    )
    _emit_result(log, telemetry_client, result)
    return result


def _emit_result(log: JsonLogger, telemetry: TelemetryClient, result: JobResult) -> None:
    fields = result.__dict__
    if result.job_status == "FAILED":
        log.error("job_completed", **fields)
    else:
        log.info("job_completed", **fields)
    telemetry.track_event("edm_job_completed", fields)
