#!/usr/bin/env bash

set -a
source .env || true
#set +a

export $1="$2"

python3 <<EOF
import os, shlex
with open(".env", 'w') as f:
    for k, v in os.environ.items():
        f.write(f"{k}={shlex.quote(v)}\n")
    k = "$1".upper()
    v = "$2"
    f.write(f"CANISTER_ID_{k}={shlex.quote(v)}\n")
EOF