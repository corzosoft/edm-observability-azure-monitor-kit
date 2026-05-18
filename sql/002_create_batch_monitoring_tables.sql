USE EdmObservabilityDemo;
GO
CREATE TABLE mon.BatchRunStatus (
    batch_run_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    correlation_id UNIQUEIDENTIFIER NOT NULL,
    job_name SYSNAME NOT NULL,
    job_status VARCHAR(30) NOT NULL,
    source_system VARCHAR(100) NULL,
    record_count INT NOT NULL DEFAULT 0,
    validation_failure_count INT NOT NULL DEFAULT 0,
    started_ts DATETIME2 NOT NULL,
    completed_ts DATETIME2 NULL,
    duration_ms BIGINT NULL,
    error_message NVARCHAR(2000) NULL
);
GO
CREATE TABLE mon.SourceFileArrival (
    file_arrival_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    correlation_id UNIQUEIDENTIFIER NULL,
    source_system VARCHAR(100) NOT NULL,
    expected_file_name VARCHAR(300) NOT NULL,
    business_date DATE NOT NULL,
    expected_by_ts DATETIME2 NOT NULL,
    arrived_ts DATETIME2 NULL,
    file_status VARCHAR(30) NOT NULL
);
GO
CREATE TABLE mon.DownstreamDistributionStatus (
    distribution_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    correlation_id UNIQUEIDENTIFIER NOT NULL,
    consumer_name VARCHAR(100) NOT NULL,
    extract_name VARCHAR(200) NOT NULL,
    distribution_status VARCHAR(30) NOT NULL,
    record_count INT NOT NULL DEFAULT 0,
    completed_ts DATETIME2 NULL,
    error_message NVARCHAR(2000) NULL
);
GO
