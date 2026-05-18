# Dynatrace Integration Notes

Azure Monitor and Dynatrace can coexist. Azure Monitor is usually the native collection and alerting surface for Azure resources, while Dynatrace can provide broader enterprise APM views across hybrid estates.

Recommended pattern:

- Keep correlation IDs consistent across Python jobs, ADF pipeline parameters, SQL monitoring rows, and downstream distribution events.
- Export application logs and custom metrics through OpenTelemetry-compatible instrumentation.
- Use Azure Monitor for Azure-native diagnostics and Dynatrace for cross-platform service health where required.
