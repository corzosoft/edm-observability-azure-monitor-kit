USE EdmObservabilityDemo;
GO
SELECT
    b.correlation_id,
    b.job_name,
    b.source_system,
    b.job_status,
    b.record_count,
    b.validation_failure_count,
    b.duration_ms,
    b.error_message,
    b.started_ts,
    b.completed_ts
FROM mon.BatchRunStatus b
WHERE b.job_status IN ('FAILED', 'SLA_BREACH')
ORDER BY b.started_ts DESC;
