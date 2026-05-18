USE EdmObservabilityDemo;
GO
CREATE OR ALTER PROCEDURE mon.usp_LogJobEnd
    @CorrelationId UNIQUEIDENTIFIER,
    @JobName SYSNAME,
    @JobStatus VARCHAR(30),
    @RecordCount INT,
    @ValidationFailureCount INT,
    @ErrorMessage NVARCHAR(2000) = NULL
AS
BEGIN
    SET NOCOUNT ON;
    UPDATE mon.BatchRunStatus
    SET job_status = @JobStatus,
        record_count = @RecordCount,
        validation_failure_count = @ValidationFailureCount,
        completed_ts = SYSUTCDATETIME(),
        duration_ms = DATEDIFF_BIG(millisecond, started_ts, SYSUTCDATETIME()),
        error_message = @ErrorMessage
    WHERE correlation_id = @CorrelationId AND job_name = @JobName;
END;
GO
