"""
Phase 1, Example 1: Basic PowerPoint Generation
Purpose: Learn to generate audit presentation slides using the PPTX skill
Scenario: Create an audit engagement overview presentation
"""

import anthropic

def create_audit_presentation():
    """Generate a presentation for audit engagement kickoff"""

    client = anthropic.Anthropic()

    print("Creating audit engagement presentation...\n")

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
                "content": """Create a professional audit engagement presentation with the following slides:

1. Title Slide: "Financial Statement Audit - Example Corporation" with subtitle "Year Ending December 31, 2024"

2. Engagement Overview:
   - Audit Scope: Full audit of financial statements
   - Standards: PCAOB and AICPA standards
   - Materiality: $500,000
   - Timeline: January - March 2025

3. Audit Team:
   - Engagement Partner: Sarah Johnson, CPA
   - Senior Manager: Michael Chen, CPA
   - Senior Auditor: Emily Rodriguez, CPA
   - Staff Auditors: James Lee, David Park

4. Key Risk Areas:
   - Revenue Recognition (High Risk)
   - Inventory Valuation (Medium Risk)
   - Related Party Transactions (Medium Risk)
   - IT General Controls (High Risk)

5. Timeline & Milestones:
   - Planning: January 2-20, 2025
   - Interim Testing: January 23 - February 10, 2025
   - Year-End Fieldwork: February 13 - March 7, 2025
   - Report Issuance: March 15, 2025

Make it professional with a clean, corporate design suitable for presenting to audit committees."""
            }
        ]
    )

    # Extract file_id from response
    file_id = None
    for block in response.content:
        if hasattr(block, 'file_id') and block.file_id:
            file_id = block.file_id
            break

    if file_id:
        print(f"File ID found: {file_id}")
        print("Downloading presentation...\n")

        # Download the file
        file_content = client.beta.files.retrieve_content(file_id)

        output_filename = "audit_engagement_presentation.pptx"
        with open(output_filename, 'wb') as f:
            f.write(file_content)

        print(f"✓ Success! Presentation saved to: {output_filename}")
        print(f"  File size: {len(file_content) / 1024:.1f} KB")

        return output_filename
    else:
        print("✗ No file generated")
        return None

if __name__ == "__main__":
    create_audit_presentation()
