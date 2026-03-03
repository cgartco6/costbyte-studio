import os
import json
from datetime import datetime
# In real repo this would import from backend.agents.prompts

print("=== AetherOS Business Generator (Cultural + Language Aware) ===")
idea = input("Describe your business idea: ")
language = input("Preferred language (af-ZA, zu-ZA, en-ZA, etc.): ") or "en-ZA"

# Simulate Master Orchestrator call
print(f"Detecting culture for {language}... (Afrikaans = braai/rugby pride, isiZulu = Ubuntu, etc.)")
site_name = idea.lower().replace(" ", "-") + "-site"

os.makedirs(f"generated_sites/{site_name}", exist_ok=True)

# Generate full responsive site (stub – real version uses prompts + LLM)
index_html = f"""
<!DOCTYPE html>
<html lang="{language}">
<head><title>{idea} – Powered by AetherOS</title></head>
<body>
<h1>{idea}</h1>
<p>Culturally perfect for you in {language}.</p>
<button onclick="alert('Payment via PayFast/PayShap/Stripe – 80% to you!')">Buy Now</button>
</body>
</html>
"""
with open(f"generated_sites/{site_name}/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

print(f"✅ Generated full site at generated_sites/{site_name}/")
print("Next: python scripts/deploy.py to push to YOUR free Netlify/Render/Vercel")

# After site generation:
print("Calling studios for full branding/marketing/design...")
os.system("python scripts/studio_generator.py")  # Or subprocess call with params
# ... (previous code after site generation)
print("Generating deliverables: PDF pack + ZIP bundle...")
pdf_bytes = generate_pdf_from_html("<h1>Test Story</h1><p>Lekker nag stories...</p>")
with open("generated/deliverables/story_pack.pdf", "wb") as f:
    f.write(pdf_bytes)

zip_buffer = create_zip_from_files(["generated/deliverables/story_pack.pdf", "generated_sites/site/index.html"])
with open("generated/deliverables/full_pack.zip", "wb") as f:
    f.write(zip_buffer.getvalue())

print("✅ PDF & ZIP ready for download in client dashboard")
