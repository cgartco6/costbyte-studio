from cryptography.fernet import Fernet
import os

# AES-256 key gen
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_data(data: str) -> str:
    return cipher.encrypt(data.encode()).decode()

def decrypt_data(encrypted: str) -> str:
    return cipher.decrypt(encrypted.encode()).decode()

# Zero-trust example: always verify user/device
def zero_trust_check(user_id, device_fingerprint):
    # Use JWT + device hash check (stub)
    return True  # In real: validate against DB

# Compliance: POPIA/GDPR log
def log_compliance_action(action: str, user_id: str):
    with open("compliance_logs.txt", "a") as f:
        f.write(f"{action} for {user_id} at {os.time()}\n")
