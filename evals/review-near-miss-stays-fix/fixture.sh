#!/usr/bin/env bash
# The shared ledger project, which has the double-count bug in total().
set -euo pipefail
bash "$(cd "$(dirname "$0")/.." && pwd)/fixture.sh"
