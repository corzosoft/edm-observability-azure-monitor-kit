# Alert: Batch SLA Breach

Trigger when a completed job exceeds its configured SLA or remains running past the expected completion time.

First checks:

- Search by correlation ID.
- Confirm whether upstream file arrival was late.
- Review SQL dependency latency and blocking.
- Check validation exception volume.
- Notify downstream consumers when publish jobs are delayed.
