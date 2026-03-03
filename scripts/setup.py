#!/usr/bin/env python3
import os, platform, subprocess

os_type = platform.system().lower()
if os_type == "linux":
    subprocess.run("sudo apt update && sudo apt install -y python3-pip git curl", shell=True)
print("Setup done")
