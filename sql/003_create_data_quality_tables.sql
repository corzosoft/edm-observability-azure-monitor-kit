USE EdmObservabilityDemo;
GO
CREATE TABLE mon.DataQualityException (
    exception_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    correlation_id UNIQUEIDENTIFIER NOT NULL,
    job_name SYSNAME NOT NULL,
    source_system VARCHAR(100) NOT NULL,
    entity_type VARCHAR(50) NOT NULL,
    entity_key VARCHAR(100) NULL,
    rule_code VARCHAR(100) NOT NULL,
    severity VARCHAR(20) NOT NULL,
    exception_message NVARCHAR(2000) NOT NULL,
    created_ts DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME()
);
GO
