#!/usr/bin/env python3
import zipfile
import os
import shutil

# Extract ZIP
with zipfile.ZipFile('/tmp/original.zip', 'r') as zip_ref:
    zip_ref.extractall('/tmp/extracted')

# List contents
print("ZIP contents:")
for root, dirs, files in os.walk('/tmp/extracted'):
    level = root.replace('/tmp/extracted', '').count(os.sep)
    indent = ' ' * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        print(f"{subindent}{file}")
