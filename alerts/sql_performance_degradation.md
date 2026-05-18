# Alert: SQL Performance Degradation

Trigger when SQL dependency latency or failed dependency count rises.

First checks:

- Review p95 latency by dependency name.
- Check blocking sessions and deadlocks.
- Review Query Store top queries.
- Confirm whether batch volume is abnormal.
