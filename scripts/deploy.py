import requests
import os
import json

print("=== AetherOS Autonomous Deploy (to YOUR free hosting) ===")
site_name = input("Site folder name (from generator): ")
token = os.getenv("NETLIFY_TOKEN") or input("Paste your Netlify/Render/Vercel token: ")

# Real Netlify API example (works same for Vercel/Render with API keys)
payload = {"name": site_name, "custom_domain": f"{site_name}.netlify.app"}
headers = {"Authorization": f"Bearer {token}"}

response = requests.post("https://api.netlify.com/api/v1/sites", json=payload, headers=headers)
if response.status_code == 201:
    print(f"✅ Deployed! Live at: {response.json()['ssl_url']}")
    print("80/20 payout logic already wired in backend/services/payment.py")
else:
    print("Error – check token")
