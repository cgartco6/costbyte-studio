import os
import platform

os_type = platform.system().lower()
host_type = input("Deploy to (local/oracle/netlify): ")

if host_type == "oracle":
    print("Using OCI CLI – ensure authenticated: oci setup config")
    os.system("oci compute instance launch --availability-domain AD1 --compartment-id your-compartment-ocid --shape VM.Standard.A1.Flex --shape-config '{\"ocpus\":4,\"memoryInGBs\":24}' --image-id ocid1.image.oc1.af-johannesburg-1.aaaaaaaawhatever --subnet-id your-subnet-ocid")
    print("VM launched – SSH and run setup")

elif host_type == "netlify":
    token = os.getenv("NETLIFY_TOKEN") or input("Netlify token: ")
    os.system(f"curl -X POST -H 'Authorization: Bearer {token}' -H 'Content-Type: application/zip' --data-binary @generated/site.zip https://api.netlify.com/api/v1/sites")

else:
    print("Local deploy – run uvicorn")

print("✅ Deployed")
