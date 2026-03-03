import os
print("=== CostByte Studio Generator ===")
studio_type = input("Design / Marketing / Branding? ").lower()
idea = input("Describe what to create: ")

folder = f"generated_studio/{studio_type}_{idea[:20]}"
os.makedirs(folder, exist_ok=True)

# Simulated AI output (real: call LLM with studio prompt)
if studio_type == "design":
    content = "<div style='background:#FF6B35;color:white;padding:40px;'><h1>AI-Generated Poster</h1><p>Culturally perfect for your idea</p></div>"
elif studio_type == "branding":
    content = "Logo prompt: minimalist mango + braai grill in orange/green\nPalette: #FF6B35, #0F172A\nFonts: Poppins + local fallback"
else:
    content = "Email sequence: Welcome → Offer → Follow-up"

with open(f"{folder}/output.html", "w") as f:
    f.write(content)

print(f"Generated in {folder}/")
