USE EdmObservabilityDemo;
GO
CREATE TABLE mon.SlaTarget (
    sla_target_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    job_name SYSNAME NOT NULL,
    source_system VARCHAR(100) NULL,
    max_duration_minutes INT NOT NULL,
    expected_completion_time TIME NULL,
    is_active BIT NOT NULL DEFAULT 1
);
GO
INSERT INTO mon.SlaTarget (job_name, source_system, max_duration_minutes, expected_completion_time)
VALUES
('file_ingestion', 'SYNTH_VENDOR_A', 30, '01:00'),
('data_quality_validation', NULL, 20, '01:30'),
('reconciliation', NULL, 45, '02:30');
GO
