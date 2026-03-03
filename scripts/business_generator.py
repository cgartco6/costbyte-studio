import os
print("=== CostByte Business Generator ===")
idea = input("Business idea: ")
lang = input("Language (e.g. af-ZA): ") or "en-ZA"

# Code swarm example (stub – real LLM call)
print("Code Swarm: Writing/Reviewing/Validating/Fixing site code...")
site_code = """<!DOCTYPE html><html><body><h1>""" + idea + """</h1></body></html>"""
with open("generated/site/index.html", "w") as f:
    f.write(site_code)

# Call document generator
os.system("python scripts/document_generator.py")

print("✅ Business generated – deploy next")
