target = input("Deploy to: ")
if target == "netlify":
    token = input("Token: ")
    os.system(f"zip -r deploy.zip generated/business && curl -X POST -H 'Authorization: Bearer {token}' --data-binary @deploy.zip https://api.netlify.com/api/v1/sites")
print("Deployed")
