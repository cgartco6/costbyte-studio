# scripts/install_dependencies.py
import os
import platform

os_type = platform.system().lower()
os.system("pip install -r backend/requirements.txt")
os.system("cd frontend && npm install")

print("✅ Deps installed")
