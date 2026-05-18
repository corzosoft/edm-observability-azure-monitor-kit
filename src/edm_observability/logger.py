from __future__ import annotations

import json
from datetime import UTC, datetime
from typing import Any, TextIO

from edm_observability.config import load_settings
from edm_observability.correlation import get_correlation_id, get_traceparent


class JsonLogger:
    def __init__(self, stream: TextIO | None = None) -> None:
        self.stream = stream
        self.settings = load_settings()

    def info(self, event_name: str, **fields: Any) -> dict[str, Any]:
        return self._write("INFO", event_name, fields)

    def error(self, event_name: str, **fields: Any) -> dict[str, Any]:
        return self._write("ERROR", event_name, fields)

    def _write(self, level: str, event_name: str, fields: dict[str, Any]) -> dict[str, Any]:
        event = {
            "timestamp": datetime.now(UTC).isoformat(),
            "level": level,
            "event_name": event_name,
            "service_name": self.settings.service_name,
            "environment": self.settings.environment,
            "correlation_id": fields.pop("correlation_id", get_correlation_id()),
            "traceparent": fields.pop("traceparent", get_traceparent()),
            **fields,
        }
        line = json.dumps(event, sort_keys=True)
        if self.stream is None:
            print(line)
        else:
            self.stream.write(line + "\n")
        return event
