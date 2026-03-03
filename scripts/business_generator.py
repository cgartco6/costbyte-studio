import os
print("Business Generator")
idea = input("Idea: ")
lang = input("Language: ") or "en-ZA"
os.makedirs("generated/business", exist_ok=True)
with open("generated/business/landing.html", "w") as f:
    f.write(f"<h1>{idea}</h1>")
print("Generated")
