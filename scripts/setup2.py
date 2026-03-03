#!/usr/bin/env python3
import os
import platform
import subprocess
import sys

def run(cmd, desc):
    print(f"🚀 {desc}")
    try:
        subprocess.check_call(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ {e}"); sys.exit(1)

print("=== AETHEROS UNIVERSAL SETUP (Any OS) ===")
print(f"OS: {platform.system()}")

run("python -m venv venv", "Creating virtual environment")
activate = "venv\\Scripts\\activate" if platform.system() == "Windows" else "source venv/bin/activate"

run(f"{activate} && pip install -r backend/requirements.txt", "Installing Python deps")
run("cd frontend && npm install", "Installing frontend deps")

if not os.path.exists(".env"):
    with open(".env.example") as src, open(".env", "w") as dst:
        dst.write(src.read())

print("🎉 SETUP COMPLETE! Now run: python scripts/business_generator.py")
