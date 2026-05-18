from __future__ import annotations

from dataclasses import dataclass
from os import getenv


@dataclass(frozen=True)
class Settings:
    service_name: str = "edm-observability-local"
    environment: str = "local"
    applicationinsights_connection_string: str = ""


def load_settings() -> Settings:
    return Settings(
        service_name=getenv("EDM_SERVICE_NAME", Settings.service_name),
        environment=getenv("EDM_ENVIRONMENT", Settings.environment),
        applicationinsights_connection_string=getenv("APPLICATIONINSIGHTS_CONNECTION_STRING", ""),
    )
