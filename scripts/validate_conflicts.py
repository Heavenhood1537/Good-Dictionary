import json,sys
from pathlib import Path
p = Path(__file__).resolve().parents[1] / 'Dictionary1.json'
try:
    with open(p,'r',encoding='utf-8') as f:
        json.load(f)
    print('JSON parse: OK')
except Exception as e:
    print('JSON parse: FAIL')
    print(e)
    sys.exit(1)

s = p.read_text(encoding='utf-8')
found = False
for m in ['<<<<<<< HEAD','=======','>>>>>>>']:
    if m in s:
        print('Found marker:', m)
        found = True
if found:
    sys.exit(1)
