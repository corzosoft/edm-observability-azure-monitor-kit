# Observability Pattern

The starter kit uses correlation-first observability. Every job emits structured JSON with the same fields: job name, status, correlation ID, source system, record count, validation failures, duration, and error message.

In Azure, these logs can be sent to Application Insights or Log Analytics through OpenTelemetry-compatible exporters. Locally, the jobs print JSON to stdout and require no Azure credentials.
