# scripts/mega_setup_install_deploy.py (Mega script – runs all in one)
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
        print(f"❌ {e}")
        sys.exit(1)

os_type = platform.system().lower()
print(f"Detected OS: {os_type}")

# Setup phase (from setup.py)
if os_type == "linux":
    run("sudo apt update && sudo apt upgrade -y", "Updating system")
    run("sudo apt install python3.12 python3.12-venv python3-pip git curl unzip -y", "Installing essentials")
elif os_type == "darwin":
    run("brew update && brew upgrade", "Updating system")
    run("brew install python@3.12 git", "Installing essentials")
elif os_type == "windows":
    print("Install Python 3.12, Git, Node.js manually from websites")

# Install deps phase (from install_dependencies.py)
run("python3 -m venv venv", "Creating venv")
activate = "venv\\Scripts\\activate" if os_type == "windows" else "source venv/bin/activate"
run(f"{activate} && pip install -r backend/requirements.txt", "Backend deps")
run("cd frontend && npm install", "Frontend deps")

# Business gen test phase (from business_generator.py)
idea = input("Test business idea: ") or "Test Business"
lang = input("Language: ") or "en-ZA"
site_code = """<html><body><h1>""" + idea + """</h1></body></html>"""
os.makedirs("generated/site", exist_ok=True)
with open("generated/site/index.html", "w") as f:
    f.write(site_code)
print("Business generated")

# Deploy phase (from deploy.py)
host = input("Deploy to (local/oracle/netlify): ") or "local"
if host == "oracle":
    run("oci compute instance launch --compartment-id your-ocid --shape VM.Standard.A1.Flex --ocpus 4 --memory-in-gbs 24 --image-id ubuntu-ocid", "Launching Oracle VM")
elif host == "netlify":
    token = os.getenv("NETLIFY_TOKEN") or input("Netlify token: ")
    run(f"curl -X POST -H 'Authorization: Bearer {token}' -H 'Content-Type: application/zip' --data-binary @generated/site.zip https://api.netlify.com/api/v1/sites", "Deploying to Netlify")
else:
    run("uvicorn app.main:app --reload", "Local deploy")

print("🎉 Mega setup/install/deploy complete!")
