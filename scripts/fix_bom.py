import os

for root, dirs, files in os.walk(r'C:\salunic-app'):
    # skip .git and __pycache__
    if '.git' in root or '__pycache__' in root or '.venv' in root:
        continue
    for fn in files:
        if fn.endswith('.py'):
            path = os.path.join(root, fn)
            try:
                with open(path, 'r', encoding='utf-8-sig') as f:
                    content = f.read()
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
            except:
                pass
print('done')
