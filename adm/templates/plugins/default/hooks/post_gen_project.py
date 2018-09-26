#!/usr/bin/env python3

import os

paths_to_delete = []
for path in [os.path.join(x[0], y) for x in os.walk('.') for y in x[2]]:
    try:
        with open(path, 'rb') as f:
            content = f.read().strip()
            if len(content) == 0:
                paths_to_delete.append(path)
    except Exception:
        pass

for path in paths_to_delete:
    if os.path.basename(path) in ['__init__.py']:
        continue
    try:
        os.unlink(path)
    except Exception:
        pass
