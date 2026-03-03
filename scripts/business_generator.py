import os
print("=== CostByte Business Generator ===")
idea = input("Idea: ")
lang = input("Language: ") or "en-ZA"

# Content/Media
os.system("python scripts/content_generator.py")

# Site
format = input("Site format (HTML5/WordPress/React): ") or "HTML5"
site_code = """<html><body><h1>""" + idea + """</h1></body></html>"""  # Real AI gen
with open("generated/site/index.html", "w") as f:
    f.write(site_code)

print("✅ Generated")
