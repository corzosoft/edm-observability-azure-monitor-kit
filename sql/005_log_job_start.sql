USE EdmObservabilityDemo;
GO
CREATE OR ALTER PROCEDURE mon.usp_LogJobStart
    @CorrelationId UNIQUEIDENTIFIER,
    @JobName SYSNAME,
    @SourceSystem VARCHAR(100) = NULL
AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO mon.BatchRunStatus (correlation_id, job_name, job_status, source_system, started_ts)
    VALUES (@CorrelationId, @JobName, 'RUNNING', @SourceSystem, SYSUTCDATETIME());
END;
GO
