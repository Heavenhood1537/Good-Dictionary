#!/usr/bin/env python3
"""
Resolve git merge conflict markers in a JSON file by keeping the second (non-HEAD) side.
Usage: python resolve_conflicts.py ../Dictionary1.json
Creates a backup at ../Dictionary1.json.bak
"""
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: resolve_conflicts.py <file>")
    sys.exit(2)

file_path = Path(sys.argv[1])
if not file_path.exists():
    print(f"File not found: {file_path}")
    sys.exit(2)

bak = file_path.with_suffix(file_path.suffix + '.bak')
# copy
import shutil
shutil.copyfile(file_path, bak)
print(f"Backup created: {bak}")

out_lines = []
with file_path.open('r', encoding='utf-8') as f:
    lines = f.readlines()

i = 0
n = len(lines)
while i < n:
    line = lines[i]
    if line.startswith('<<<<<<< HEAD'):
        # skip until '=======\n'
        i += 1
        while i < n and not lines[i].startswith('======='):
            i += 1
        # now at =======
        if i >= n:
            print('Malformed conflict: missing =======')
            sys.exit(1)
        i += 1
        # collect right side until >>>>>>>
        right_side = []
        while i < n and not lines[i].startswith('>>>>>>>'):
            right_side.append(lines[i])
            i += 1
        if i >= n:
            print('Malformed conflict: missing >>>>>>>')
            sys.exit(1)
        # append right_side to out
        out_lines.extend(right_side)
        i += 1
        continue
    else:
        out_lines.append(line)
        i += 1

# Write back
with file_path.open('w', encoding='utf-8') as f:
    f.writelines(out_lines)

print(f"Conflicts resolved in: {file_path}")
