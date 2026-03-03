#!/usr/bin/env python3
import os
import platform
import subprocess
import sys

def run(cmd, desc, shell=True):
    print(f"🚀 {desc}")
    try:
        subprocess.check_call(cmd, shell=shell)
    except Exception as e:
        print(f"❌ Failed: {e}")
        sys.exit(1)

os_type = platform.system().lower()
print(f"Detected OS: {os_type}")

# Check & install Python (assume 3.12+ – prompt manual if missing)
if not '3.12' in sys.version:
    print("Install Python 3.12 manually from python.org or apt/brew/choco")
    sys.exit(1)

# Check & install Git
if os.system("git --version") != 0:
    if os_type == "linux":
        run("sudo apt install git -y", "Installing Git")
    elif os_type == "darwin":
        run("brew install git", "Installing Git – brew required")
    elif os_type == "windows":
        print("Download Git from git-scm.com and run installer")

# Check & install Node.js/npm
if os.system("node --version") != 0:
    if os_type == "linux":
        run("curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - && sudo apt install -y nodejs", "Installing Node.js 20")
    elif os_type == "darwin":
        run("brew install node@20", "Installing Node.js 20")
    elif os_type == "windows":
        print("Download Node.js 20 LTS from nodejs.org and run installer")

# Check & install Oracle CLI (for Oracle deploy)
if os.system("oci --version") != 0:
    if os_type == "linux":
        run("curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.py | python3 -", "Installing Oracle CLI")
    elif os_type == "darwin":
        run("brew install oracle/oci-cli/oci-cli", "Installing Oracle CLI")
    elif os_type == "windows":
        print("Download OCI CLI from oracle.com and run installer")

# Create venv & install backend deps
run("python3 -m venv venv", "Creating virtual environment")
activate = "venv\\Scripts\\activate" if os_type == "windows" else "source venv/bin/activate"
run(f"{activate} && pip install -r backend/requirements.txt", "Installing backend deps")

# Frontend
run("cd frontend && npm install", "Installing frontend deps")

print("🎉 Setup complete! Run python scripts/business_generator.py to test")
