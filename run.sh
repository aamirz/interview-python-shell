#!/usr/bin/env bash
set -euo pipefail

docker run -it \
    --mount type=bind,source="$(pwd)"/scripts,target=/scripts \
    --name python-interview-container python-interview-image bash
