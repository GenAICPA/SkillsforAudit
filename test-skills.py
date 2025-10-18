import anthropic
import json

print("Starting script...")
client = anthropic.Anthropic()
print("Client created, sending request to API...")

response = client.beta.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02", "files-api-2025-04-14"],
    container={
        "skills": [
            {
                "type": "anthropic",
                "skill_id": "pptx",
                "version": "latest"
            }
        ]
    },
    tools=[
        {
            "type": "code_execution_20250825",
            "name": "code_execution"
        }
    ],
    messages=[
        {
            "role": "user",
            "content": "Create a presentation about renewable energy with 3 slides covering solar, wind, and hydroelectric power"
        }
    ]
)

print("Response received!")
print("\n=== Response Object Type ===")
print(type(response))

print("\n=== Response Content ===")
print(f"Number of content blocks: {len(response.content)}")

for i, block in enumerate(response.content):
    print(f"\n--- Block {i} ---")
    print(f"Block type: {type(block)}")
    print(f"Block attributes: {dir(block)}")
    print(f"Block as dict: {block.model_dump() if hasattr(block, 'model_dump') else block}")

print("\n=== Full Response Dump ===")
try:
    print(json.dumps(response.model_dump(), indent=2, default=str))
except Exception as e:
    print(f"Could not JSON dump: {e}")
    print(response)