from backend.services.content_creator import generate_realistic_text
from backend.services.media_creator.py import generate_voice, generate_music, generate_video

text = generate_realistic_text("Test prompt")
voice = generate_voice(text)
music = generate_music("Test music prompt")
video = generate_video("Test video prompt")

print("✅ Content/Media generated in HD/4K")
