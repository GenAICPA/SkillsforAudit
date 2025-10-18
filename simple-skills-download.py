import anthropic

client = anthropic.Anthropic()

print("Creating presentation with Skills (simplified approach)...\n")

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
            "content": "Create a presentation about renewable energy with 3 slides covering solar, wind, and hydroelectric power. Make it professional and visually appealing."
        }
    ]
)

print("=== Response Analysis ===\n")

# Look through all content blocks
file_id = None
for i, block in enumerate(response.content):
    if block.type == 'text':
        text_preview = block.text[:150] + "..." if len(block.text) > 150 else block.text
        print(f"Block {i} (text): {text_preview}\n")
    
    # Check for file_id in various block types
    if hasattr(block, 'file_id') and block.file_id:
        file_id = block.file_id
        print(f"Block {i}: Found file_id: {file_id}\n")

# If no file_id found in blocks, check the response structure more carefully
if not file_id:
    print("No file_id found in content blocks.")
    print("\nFull response structure:")
    print(response.model_dump_json(indent=2))
else:
    print(f"\n=== Downloading File ===\n")
    print(f"File ID: {file_id}")
    
    try:
        file_content = client.beta.files.retrieve_content(file_id)
        
        output_filename = "renewable_energy_presentation.pptx"
        with open(output_filename, 'wb') as f:
            f.write(file_content)
        
        print(f"✓ Success! File downloaded to: {output_filename}")
        print(f"  File size: {len(file_content)} bytes ({len(file_content) / 1024:.1f} KB)")
        
    except Exception as e:
        print(f"✗ Error downloading file: {e}")