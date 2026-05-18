IF DB_ID('EdmObservabilityDemo') IS NULL CREATE DATABASE EdmObservabilityDemo;
GO
USE EdmObservabilityDemo;
GO
IF NOT EXISTS (SELECT 1 FROM sys.schemas WHERE name = 'mon') EXEC('CREATE SCHEMA mon');
GO
