from __future__ import annotations

import argparse

from edm_observability.correlation import new_correlation_id
from edm_observability.sample_file_ingestion_job import run_file_ingestion_job
from edm_observability.sample_reconciliation_job import (
    run_data_quality_validation_job,
    run_reconciliation_job,
)


def main() -> None:
    parser = argparse.ArgumentParser(prog="edm-observe")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("run-file-ingestion")
    subparsers.add_parser("run-data-quality")
    reconciliation = subparsers.add_parser("run-reconciliation")
    reconciliation.add_argument("--fail", action="store_true")

    args = parser.parse_args()
    new_correlation_id()
    if args.command == "run-file-ingestion":
        run_file_ingestion_job()
    elif args.command == "run-data-quality":
        run_data_quality_validation_job()
    else:
        run_reconciliation_job(fail=args.fail)


if __name__ == "__main__":
    main()
