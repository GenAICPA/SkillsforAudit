import anthropic

client = anthropic.Anthropic()

print("Creating presentation with Skills...")

response = client.beta.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=2048,
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
            "content": "Create a presentation about renewable energy with 3 slides covering solar, wind, and hydroelectric power."
        }
    ]
)

print("\n=== Response received ===")
print(f"Number of content blocks: {len(response.content)}\n")

# Look for file references in the response
file_id = None
for i, block in enumerate(response.content):
    print(f"Block {i}: {block.type}")
    if hasattr(block, 'text'):
        print(f"  Text: {block.text[:100]}..." if len(block.text) > 100 else f"  Text: {block.text}")
    if hasattr(block, 'file_id'):
        file_id = block.file_id
        print(f"  File ID: {file_id}")
    print()

# Try to download the file if we found a file_id
if file_id:
    print(f"\n=== Downloading file {file_id} ===")
    try:
        file_content = client.beta.files.retrieve_content(file_id)
        
        output_filename = "renewable_energy_presentation.pptx"
        with open(output_filename, 'wb') as f:
            f.write(file_content)
        
        print(f"✓ File downloaded successfully to: {output_filename}")
        print(f"  File size: {len(file_content)} bytes")
    except Exception as e:
        print(f"✗ Error downloading file: {e}")
else:
    print("\n✗ No file_id found in response")
    print("Full response dump:")
    print(response.model_dump_json(indent=2))