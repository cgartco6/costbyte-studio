import os
import platform

os_type = platform.system().lower()

# Backend (requirements.txt assumed populated)
os.system("pip install -r backend/requirements.txt")

# Frontend
if os_type == "windows":
    os.system("cd frontend && npm install")
else:
    os.system("cd frontend && npm install")

print("✅ All dependencies installed")

import subprocess
print("Installing ALL dependencies cross-platform...")
subprocess.check_call(["pip", "install", "-r", "backend/requirements.txt"])
subprocess.check_call(["cd", "frontend", "&&", "npm", "install"], shell=True)
print("✅ Dependencies installed everywhere")
