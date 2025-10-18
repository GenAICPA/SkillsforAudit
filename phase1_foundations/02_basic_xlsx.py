"""
Phase 1, Example 2: Excel Workpaper Generation
Purpose: Learn to generate audit workpapers using the XLSX skill
Scenario: Create a bank reconciliation workpaper template
"""

import anthropic

def create_bank_reconciliation_workpaper():
    """Generate an Excel workpaper for bank reconciliation testing"""

    client = anthropic.Anthropic()

    print("Creating bank reconciliation workpaper...\n")

    response = client.beta.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=3096,
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
                "content": """Create a professional audit workpaper in Excel for bank reconciliation testing with the following structure:

Sheet 1 - "Bank Reconciliation":
Client: Example Corporation
Account: Cash - Operating Account #4521
Period End: December 31, 2024
Prepared by: [blank]
Reviewed by: [blank]

Include these sections with sample data:
1. Bank Balance per Statement: $1,245,680.50
2. Add: Deposits in Transit
   - Dec 30: $45,000
   - Dec 31: $32,500
3. Less: Outstanding Checks
   - Check #8843: $12,300
   - Check #8851: $8,750
   - Check #8856: $5,200
4. Adjusted Bank Balance: [formula]
5. Book Balance per GL: $1,297,430.50
6. Adjustments to Book Balance: [section for entries]
7. Adjusted Book Balance: [formula]
8. Difference: [formula - should be $0]

Sheet 2 - "Outstanding Checks Detail":
List outstanding checks with columns:
- Check Number
- Date
- Payee
- Amount
- Days Outstanding
- Cleared in Jan? (Y/N)

Sheet 3 - "Deposits in Transit":
List deposits with columns:
- Date
- Description
- Amount
- Cleared in Jan? (Y/N)

Sheet 4 - "Audit Procedures":
Create a checklist with these procedures:
- Obtain bank confirmation
- Verify mathematical accuracy
- Test deposits in transit (cleared subsequently?)
- Test outstanding checks (cleared subsequently?)
- Review for unusual items
- Verify bank reconciliation preparer/reviewer sign-offs

Use professional formatting with:
- Header with client name and period
- Proper accounting number formats (currency with 2 decimals)
- Borders and shading for sections
- Formula cells highlighted in light yellow
- Input cells with light blue background
- Include a "WP Reference: A-1" in the header"""
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
        print("Downloading workpaper...\n")

        # Download the file
        file_content = client.beta.files.retrieve_content(file_id)

        output_filename = "bank_reconciliation_workpaper.xlsx"
        with open(output_filename, 'wb') as f:
            f.write(file_content)

        print(f"✓ Success! Workpaper saved to: {output_filename}")
        print(f"  File size: {len(file_content) / 1024:.1f} KB")

        return output_filename
    else:
        print("✗ No file generated")
        return None

if __name__ == "__main__":
    create_bank_reconciliation_workpaper()
