#!/usr/bin/env python3

import re
import sys
from collections import OrderedDict
import shlex

envre = re.compile(r'''^([^=]+)\s*?=\s*?(.*)$''')
result = OrderedDict()
try:
    with open(".env") as ins:
        for line in ins:
            match = envre.match(line)
            if match is not None:
                result[match.group(1)] = match.group(2)
except FileNotFoundError:
    pass

c = sys.argv[1].upper()
v = sys.argv[2]
result[f"CANISTER_ID_{c}"] = shlex.quote(v)

with open(".env", 'w') as out:
    for k, v in result.items():
        out.write(f"{k}={v}\n")
