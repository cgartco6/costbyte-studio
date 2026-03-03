#!/usr/bin/env python3
"""
CostByte Mega Autonomous Script – Setup, Install, Deploy, Test on ANY OS
"""

import os
import platform
import subprocess
import sys

os_type = platform.system().lower()
print(f"CostByte Mega – OS: {os_type}")

def run(cmd, desc, shell=True):
    print(f"🚀 {desc}")
    try:
        subprocess.check_call(cmd, shell=shell)
    except Exception as e:
        print(f"❌ {e}")
        sys.exit(1)

# SETUP PHASE
print("SETUP PHASE")
if os_type == "linux":
    run("sudo apt update && sudo apt upgrade -y", "Update")
    run("sudo apt install -y python3.12 python3-pip python3-venv git curl unzip", "Essentials")
elif os_type == "darwin":
    run("brew update && brew install python git node", "Essentials")
elif os_type == "windows":
    print("Install Python/Git/Node manually")

# INSTALL PHASE
print("INSTALL PHASE")
run("python3 -m venv venv", "Venv")
activate = "venv\\Scripts\\activate" if os_type == "windows" else "source venv/bin/activate"
run(f"{activate} && pip install -r backend/requirements.txt", "Backend deps")
run("cd frontend && npm install", "Frontend deps")

# GENERATION PHASE
print("GENERATION PHASE")
idea = input("Idea: ") or "Test"
lang = input("Language: ") or "en-ZA"
os.makedirs("generated/site", exist_ok=True)
with open("generated/site/index.html", "w") as f:
    f.write(f"<h1>{idea}</h1>")
run("python scripts/content_generator.py", "Content gen")

# DEPLOY PHASE
print("DEPLOY PHASE")
target = input("Deploy to (local/oracle/netlify): ") or "local"
if target == "oracle":
    print("Oracle – SSH to VM and run this script there")
elif target == "netlify":
    token = input("Netlify token: ")
    run("zip -r deploy.zip generated/site", "Zipping")
    run(f"curl -X POST -H 'Authorization: Bearer {token}' --data-binary @deploy.zip https://api.netlify.com/api/v1/sites", "Netlify deploy")
else:
    run(f"{activate} && uvicorn backend.app.main:app --reload --port 8000", "Local server")

print("🎉 Mega complete!")
