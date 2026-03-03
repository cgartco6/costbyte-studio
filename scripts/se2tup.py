#!/usr/bin/env python3
import os
import platform
import subprocess
import sys

os_type = platform.system().lower()

def check_install(cmd, install_cmd, desc):
    if os.system(cmd) != 0:
        run(install_cmd, "Installing " + desc)

def run(cmd, desc):
    print(f"🚀 {desc}")
    subprocess.check_call(cmd, shell=True)

check_install("python3 --version", "sudo apt install python3.12 -y" if os_type == "linux" else "echo Install Python manually", "Python")
check_install("git --version", "sudo apt install git -y" if os_type == "linux" else "echo Install Git manually", "Git")
check_install("node --version", "curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - && sudo apt install -y nodejs" if os_type == "linux" else "echo Install Node.js manually", "Node.js")

# Venv & deps
run("python3 -m venv venv", "Creating venv")
activate = "venv\\Scripts\\activate" if os_type == "windows" else "source venv/bin/activate"
run(f"{activate} && pip install -r backend/requirements.txt", "Backend deps")
run("cd frontend && npm install", "Frontend deps")

print("🎉 Setup complete")
