# Production Runbook

## Triage Flow

1. Start with the alert and copy the correlation ID.
2. Run the end-to-end KQL trace.
3. Identify whether the failure is ingestion, validation, reconciliation, SQL, or distribution.
4. Check SLA impact and downstream consumers.
5. Decide on rerun, wait, vendor escalation, or downstream notification.
6. Record incident notes, root cause, and preventive action.

## Common Actions

- Missing file: validate expected schedule, check vendor channel, rerun ingestion after arrival.
- High DQ exceptions: compare to baseline, sample records, escalate to data steward if needed.
- SQL slowness: check dependencies, blocking, Query Store, and recent deployments.
- Distribution failure: confirm extract generation, storage permissions, and consumer endpoint status.
