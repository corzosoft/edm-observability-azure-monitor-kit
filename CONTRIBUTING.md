# Contributing

This repository demonstrates observability patterns for EDM-style Azure data platforms.

Guidelines:

- Use fake data and synthetic events only.
- Do not add real production telemetry, customer identifiers, or credentials.
- Keep local examples runnable without Azure credentials.
- Add tests for Python correlation, logging, telemetry, and sample job behavior.
- Document where real Azure configuration is required.

Before opening a pull request:

```powershell
python -m pytest
python -m ruff check .
```
