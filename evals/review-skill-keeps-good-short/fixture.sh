#!/usr/bin/env bash
# Copies this case's input files into the empty workspace.
set -euo pipefail
cp -R "$(dirname "$0")/files/." .
