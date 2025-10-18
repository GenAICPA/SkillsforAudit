"""
Phase 2, Example 6: Generate Excel Workpapers from Structured Data
Purpose: Transform JSON audit checklist into formatted Excel workpapers using Skills
Scenario: Automated workpaper generation from audit program
"""

import anthropic
import json

def generate_excel_from_checklist(checklist_file: str = "sample_audit_checklist.json"):
    """Generate Excel workpaper from audit checklist JSON"""

    # Load the checklist
    try:
        with open(checklist_file, 'r', encoding='utf-8') as f:
            checklist = json.load(f)
    except FileNotFoundError:
        print(f"✗ Error: Checklist file not found: {checklist_file}")
        print("Run 04_audit_checklist_model.py first to create sample data")
        return None

    engagement = checklist["audit_engagement"]

    print(f"Generating Excel workpaper for: {engagement['client']}\n")

    # Build detailed prompt with checklist data
    prompt = f"""Create a comprehensive audit workpaper in Excel based on this audit checklist data:

CLIENT: {engagement['client']}
PERIOD END: {engagement['period_end']}
ENGAGEMENT PARTNER: {engagement['engagement_partner']}
MATERIALITY: ${engagement['materiality']:,}

Create the following sheets:

Sheet 1 - "Audit Summary":
- Engagement overview (client, period, partner, materiality)
- Overall completion statistics
- Summary table showing each audit section with:
  * Section ID and Name
  * Risk Level (use color coding: red=high, yellow=medium, green=low)
  * Total Procedures
  * Completed Procedures
  * % Complete
  * Procedures with exceptions

"""

    # Add details for each section
    for i, section in enumerate(engagement["sections"], start=2):
        prompt += f"""
Sheet {i} - "{section['name']}":
Section ID: {section['section_id']}
Risk Level: {section['risk_level'].upper()}
Description: {section.get('description', 'N/A')}

Procedure details table with these columns:
| Proc ID | Description | Assigned To | Due Date | Status | WP Ref | Evidence | XBRL Links | Sign-Off | Notes |

Data rows:
"""
        for proc in section["procedures"]:
            status_display = proc['status'].replace('_', ' ').title()
            assigned = proc.get('assigned_to', 'Unassigned')
            due = proc.get('due_date', 'TBD')
            wp_ref = proc.get('workpaper_ref', 'N/A')
            evidence = ', '.join(proc.get('evidence_refs', []))[:30]
            xbrl = ', '.join(proc.get('xbrl_refs', []))[:40]

            sign_off_info = ""
            notes = ""
            if 'sign_off' in proc:
                so = proc['sign_off']
                sign_off_info = f"{so.get('auditor', 'N/A')} on {so.get('date', 'N/A')}"
                notes = so.get('notes', '')[:50]

            prompt += f"""
- {proc['procedure_id']}: {proc['description']} | {assigned} | {due} | {status_display} | {wp_ref} | {evidence} | {xbrl} | {sign_off_info} | {notes}
"""

    # Add XBRL cross-reference sheet
    prompt += f"""

Sheet {len(engagement['sections']) + 2} - "XBRL Cross-Reference":
Create a table mapping XBRL elements to audit procedures:
| XBRL Element | Procedure IDs | Audit Sections | Status |

"""

    # Collect XBRL mappings
    xbrl_map = {}
    for section in engagement["sections"]:
        for proc in section["procedures"]:
            if 'xbrl_refs' in proc:
                for xbrl_ref in proc['xbrl_refs']:
                    if xbrl_ref not in xbrl_map:
                        xbrl_map[xbrl_ref] = {"procs": [], "sections": set(), "statuses": []}
                    xbrl_map[xbrl_ref]["procs"].append(proc['procedure_id'])
                    xbrl_map[xbrl_ref]["sections"].add(section['section_id'])
                    xbrl_map[xbrl_ref]["statuses"].append(proc['status'])

    for xbrl_element, data in sorted(xbrl_map.items()):
        procs = ', '.join(data['procs'])
        sections = ', '.join(sorted(data['sections']))
        all_completed = all(s == 'completed' for s in data['statuses'])
        status = "Complete" if all_completed else "In Progress"
        prompt += f"- {xbrl_element} | {procs} | {sections} | {status}\n"

    prompt += """

Formatting requirements:
- Professional header on each sheet with client name and period
- Use filters on all data tables
- Conditional formatting for status (green=completed, yellow=in progress, gray=not started)
- Color coding for risk levels (red=high, yellow=medium, green=low)
- Freeze top row headers
- Auto-fit column widths
- Add borders to all tables
- Include preparer/reviewer signature blocks at bottom of each sheet
- Include current date and workpaper reference numbers

Make it look professional and audit-ready."""

    # Call Claude with XLSX skill
    client = anthropic.Anthropic()

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
        messages=[{"role": "user", "content": prompt}]
    )

    # Extract and download file
    file_id = None
    for block in response.content:
        if hasattr(block, 'file_id') and block.file_id:
            file_id = block.file_id
            break

    if file_id:
        print(f"File ID found: {file_id}")
        print("Downloading workpaper...\n")

        file_content = client.beta.files.retrieve_content(file_id)

        output_filename = f"audit_program_{engagement['client'].replace(' ', '_')}.xlsx"
        with open(output_filename, 'wb') as f:
            f.write(file_content)

        print(f"✓ Success! Audit program workpaper saved to: {output_filename}")
        print(f"  File size: {len(file_content) / 1024:.1f} KB")
        print(f"  Sections: {len(engagement['sections'])}")
        print(f"  Total procedures: {sum(len(s['procedures']) for s in engagement['sections'])}")

        return output_filename
    else:
        print("✗ No file generated")
        for block in response.content:
            if block.type == 'text':
                print(f"\nClaude's response:\n{block.text[:300]}...")
        return None

if __name__ == "__main__":
    # Generate sample data if needed
    try:
        with open("sample_audit_checklist.json", 'r') as f:
            pass
    except FileNotFoundError:
        print("Sample checklist not found. Creating it first...\n")
        import sys
        import os
        # Adjust path to find the module
        sys.path.insert(0, os.path.dirname(__file__))
        import audit_checklist_model as model
        model.save_sample_checklist()
        print()

    # Generate Excel workpaper
    generate_excel_from_checklist()
