#!/usr/bin/env python3
"""
Repackage this skill into a distributable zip file.

Usage:
    cd debug
    python repackage.py

Output: ../debug.zip
"""
import zipfile
from pathlib import Path

# Paths relative to this script
script_dir = Path(__file__).parent
skill_name = script_dir.name
zip_path = script_dir.parent / f'{skill_name}.zip'

# Remove old zip if exists
if zip_path.exists():
    zip_path.unlink()
    print(f"Removed old: {zip_path.name}")

print(f"Packaging skill: {skill_name}\n")

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for file_path in script_dir.rglob('*'):
        if file_path.is_file() and file_path.name != 'repackage.py':  # Don't include this script
            arcname = file_path.relative_to(script_dir.parent)
            zf.write(file_path, arcname)
            print(f"  Added: {arcname}")

print(f"\n✅ Successfully packaged to: {zip_path.absolute()}")
