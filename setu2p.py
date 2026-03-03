#!/usr/bin/env python3
import os
import platform
import subprocess
import sys

def run_command(cmd, desc):
    print(f"🚀 {desc}")
    try:
        subprocess.check_call(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed: {e}")
        sys.exit(1)

print("=== AetherOS Cross-Platform Setup (2026) ===")
print(f"Detected OS: {platform.system()} {platform.release()}")

# 1. Create virtual env
run_command("python -m venv venv", "Creating Python virtual environment...")
if platform.system() == "Windows":
    activate = "venv\\Scripts\\activate"
else:
    activate = "source venv/bin/activate"

# 2. Install dependencies
run_command(f"{activate} && pip install -r backend/requirements.txt", "Installing backend deps...")
run_command("cd frontend && npm install", "Installing frontend deps...")  # or pnpm if preferred

# 3. Copy env example
if not os.path.exists(".env"):
    with open(".env.example") as f:
        open(".env", "w").write(f.read())
    print("✅ .env created from example")

print("🎉 AetherOS is ready! Run: python scripts/business_generator.py to launch a client business")
