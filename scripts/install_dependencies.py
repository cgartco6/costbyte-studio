import subprocess
print("Installing ALL dependencies cross-platform...")
subprocess.check_call(["pip", "install", "-r", "backend/requirements.txt"])
subprocess.check_call(["cd", "frontend", "&&", "npm", "install"], shell=True)
print("✅ Dependencies installed everywhere")
