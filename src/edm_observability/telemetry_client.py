from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from edm_observability.config import Settings, load_settings


@dataclass
class TelemetryClient:
    """Local placeholder for Azure Monitor / OpenTelemetry compatible events."""

    settings: Settings = field(default_factory=load_settings)
    emitted_events: list[dict[str, Any]] = field(default_factory=list)

    def track_event(self, name: str, properties: dict[str, Any]) -> None:
        self.emitted_events.append(
            {
                "name": name,
                "properties": properties,
                "exporter": "local-placeholder",
                "azure_monitor_configured": bool(
                    self.settings.applicationinsights_connection_string
                ),
            }
        )
