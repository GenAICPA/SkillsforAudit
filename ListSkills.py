import os
from anthropic import Anthropic

# Initialize the Anthropic client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# List Anthropic built-in skills
print("=== ANTHROPIC SKILLS ===")
skills = client.beta.skills.list(source="anthropic")
for s in skills.data:
    print(f"{s.id:30s} {s.display_title}")

# List custom skills
print("\n=== CUSTOM SKILLS ===")
custom_skills = client.beta.skills.list(source="custom")
if custom_skills.data:
    for s in custom_skills.data:
        print(f"{s.id:30s} {s.display_title}")
else:
    print("(No custom skills found)")
