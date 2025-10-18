"""
Phase 1, Example 3: Code Execution with Skills
Purpose: Learn to manipulate data with code execution before generating documents
Scenario: Calculate audit sampling sizes and generate Excel documentation
"""

import anthropic

def create_sampling_workpaper():
    """Use code execution to calculate statistical samples, then generate Excel workpaper"""

    client = anthropic.Anthropic()

    print("Calculating audit samples and generating workpaper...\n")

    response = client.beta.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=4096,
        betas=["code-execution-2025-08-25", "skills-2025-10-02", "files-api-2025-04-14"],
        container={
            "skills": [
                {
                    "type": "anthropic",
                    "skill_id": "xlsx",
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
                "content": """You are assisting with audit sampling calculations.

First, use code execution to calculate appropriate sample sizes for these audit populations:

Population 1 - Revenue Transactions:
- Total population: 8,450 transactions
- Total dollar value: $12,500,000
- Risk assessment: High
- Expected error rate: 2%
- Confidence level: 95%
- Tolerable error rate: 5%

Population 2 - Accounts Payable:
- Total population: 2,340 invoices
- Total dollar value: $3,200,000
- Risk assessment: Medium
- Expected error rate: 1%
- Confidence level: 95%
- Tolerable error rate: 5%

Population 3 - Fixed Asset Additions:
- Total population: 156 additions
- Total dollar value: $2,800,000
- Risk assessment: Low
- Expected error rate: 0%
- Confidence level: 90%
- Tolerable error rate: 5%

Use the attribute sampling formula for calculating sample sizes. For populations under 250 items with low risk, use 100% testing or systematic selection.

After calculating sample sizes, create an Excel workpaper with:

Sheet 1 - "Sampling Summary":
- Table showing all three populations with calculated sample sizes
- Methodology notes
- Sample selection method (random, systematic, or judgmental)
- Preparer and reviewer signature blocks

Sheet 2 - "Revenue Sample Selection":
- Column headers: Sample #, Transaction ID, Date, Customer, Amount, Selected for Testing
- Generate random sample selections based on calculated size
- Include formulas for sample size calculation

Sheet 3 - "AP Sample Selection":
- Similar structure for AP testing

Sheet 4 - "Fixed Assets Selection":
- Similar structure (may be 100% if population is small)

Sheet 5 - "Methodology":
- Explain attribute sampling
- Document risk assessments
- Show formulas used
- Reference AICPA Audit Sampling Guide

Format professionally with:
- Clear headers and borders
- Color coding by risk level (red=high, yellow=medium, green=low)
- Formulas visible where applicable
- Workpaper reference: C-3"""
            }
        ]
    )

    # Extract file_id from response
    file_id = None
    print("Response content blocks:")
    for i, block in enumerate(response.content):
        print(f"  Block {i}: {block.type}")
        if hasattr(block, 'file_id') and block.file_id:
            file_id = block.file_id
            print(f"    ↳ File ID: {file_id}")

    if file_id:
        print(f"\nDownloading workpaper...\n")

        # Download the file
        file_content = client.beta.files.retrieve_content(file_id)

        output_filename = "audit_sampling_workpaper.xlsx"
        with open(output_filename, 'wb') as f:
            f.write(file_content)

        print(f"✓ Success! Sampling workpaper saved to: {output_filename}")
        print(f"  File size: {len(file_content) / 1024:.1f} KB")

        return output_filename
    else:
        print("✗ No file generated")
        # Print text response for debugging
        for block in response.content:
            if block.type == 'text':
                print("\nClaude's response:")
                print(block.text[:500] + "..." if len(block.text) > 500 else block.text)
        return None

if __name__ == "__main__":
    create_sampling_workpaper()
