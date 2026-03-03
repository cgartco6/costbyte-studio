# scripts/setup.py
#!/usr/bin/env python3
import os
import platform
import subprocess
import sys

os_type = platform.system().lower()

def run(cmd, desc):
    print(f"🚀 {desc}")
    subprocess.check_call(cmd, shell=True)

if os_type == "linux":
    run("sudo apt update && sudo apt upgrade -y", "Updating")
    run("sudo apt install python3.12 python3-pip git curl -y", "Essentials")
elif os_type == "windows":
    print("Install Python/Git/Node manually")

run("python3 -m venv venv", "Venv")
print("✅ Setup complete")
