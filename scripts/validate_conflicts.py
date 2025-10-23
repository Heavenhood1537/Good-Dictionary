import json,sys
p = r'c:\Users\milan\Documents\1_Desktop\Good-Dictionary\Dictionary1.json'
try:
    with open(p,'r',encoding='utf-8') as f:
        json.load(f)
    print('JSON parse: OK')
except Exception as e:
    print('JSON parse: FAIL')
    print(e)
    sys.exit(1)

s = open(p,'r',encoding='utf-8').read()
for m in ['<<<<<<< HEAD','=======','>>>>>>>']:
    if m in s:
        print('Found marker:', m)
