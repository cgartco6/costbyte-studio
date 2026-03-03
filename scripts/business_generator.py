# scripts/deploy.py
import os

host = input("Deploy to (local/oracle/netlify): ")
if host == "oracle":
    os.system("oci compute instance launch --shape VM.Standard.A1.Flex --ocpus 4 --memory-in-gbs 24 --image-id ubuntu-ocid")
elif host == "netlify":
    token = os.getenv("NETLIFY_TOKEN") or input("Token: ")
    os.system(f"curl -X POST -H 'Authorization: Bearer {token}' -H 'Content-Type: application/zip' --data-binary @generated/site.zip https://api.netlify.com/api/v1/sites")
else:
    os.system("uvicorn app.main:app --reload")

print("✅ Deployed")
