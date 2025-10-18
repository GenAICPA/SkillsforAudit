"""
Phase 2, Example 5: JSON Schema Validation
Purpose: Validate audit checklist data against schema
Scenario: Ensure data quality before processing
"""

import json
import sys

def validate_checklist_simple(checklist_data: dict) -> tuple[bool, list]:
    """
    Simple validation without external dependencies
    Returns: (is_valid, errors)
    """
    errors = []

    # Check required top-level fields
    if "version" not in checklist_data:
        errors.append("Missing required field: version")
    if "audit_engagement" not in checklist_data:
        errors.append("Missing required field: audit_engagement")
        return False, errors

    engagement = checklist_data["audit_engagement"]

    # Check required engagement fields
    required_fields = ["client", "period_end", "engagement_partner", "sections"]
    for field in required_fields:
        if field not in engagement:
            errors.append(f"Missing required field: audit_engagement.{field}")

    # Validate sections
    if "sections" in engagement:
        for i, section in enumerate(engagement["sections"]):
            section_path = f"sections[{i}]"

            # Check required section fields
            if "section_id" not in section:
                errors.append(f"{section_path}: Missing section_id")
            if "name" not in section:
                errors.append(f"{section_path}: Missing name")
            if "procedures" not in section:
                errors.append(f"{section_path}: Missing procedures")
                continue

            # Validate risk level
            if "risk_level" in section:
                if section["risk_level"] not in ["low", "medium", "high"]:
                    errors.append(f"{section_path}: Invalid risk_level '{section['risk_level']}'")

            # Validate procedures
            for j, procedure in enumerate(section["procedures"]):
                proc_path = f"{section_path}.procedures[{j}]"

                # Check required procedure fields
                if "procedure_id" not in procedure:
                    errors.append(f"{proc_path}: Missing procedure_id")
                if "description" not in procedure:
                    errors.append(f"{proc_path}: Missing description")
                if "status" not in procedure:
                    errors.append(f"{proc_path}: Missing status")
                elif procedure["status"] not in ["not_started", "in_progress", "completed", "not_applicable"]:
                    errors.append(f"{proc_path}: Invalid status '{procedure['status']}'")

                # Validate XBRL references format
                if "xbrl_refs" in procedure:
                    if not isinstance(procedure["xbrl_refs"], list):
                        errors.append(f"{proc_path}: xbrl_refs must be an array")

                # Validate sign-off if present
                if "sign_off" in procedure:
                    sign_off = procedure["sign_off"]
                    if procedure["status"] == "completed":
                        if "auditor" not in sign_off:
                            errors.append(f"{proc_path}: Completed procedure missing sign_off.auditor")
                        if "date" not in sign_off:
                            errors.append(f"{proc_path}: Completed procedure missing sign_off.date")

    return len(errors) == 0, errors

def load_and_validate_checklist(filename: str):
    """Load checklist from file and validate"""
    print(f"Loading checklist from: {filename}\n")

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            checklist = json.load(f)
    except FileNotFoundError:
        print(f"✗ Error: File not found: {filename}")
        return False
    except json.JSONDecodeError as e:
        print(f"✗ Error: Invalid JSON: {e}")
        return False

    print("Validating checklist structure...\n")
    is_valid, errors = validate_checklist_simple(checklist)

    if is_valid:
        print("✓ Validation PASSED")
        print(f"  Client: {checklist['audit_engagement']['client']}")
        print(f"  Period: {checklist['audit_engagement']['period_end']}")

        # Count procedures
        total_procedures = sum(
            len(section["procedures"])
            for section in checklist["audit_engagement"]["sections"]
        )
        print(f"  Total procedures: {total_procedures}")

        # Count XBRL references
        total_xbrl_refs = 0
        for section in checklist["audit_engagement"]["sections"]:
            for proc in section["procedures"]:
                if "xbrl_refs" in proc:
                    total_xbrl_refs += len(proc["xbrl_refs"])
        print(f"  XBRL references: {total_xbrl_refs}")

        return True
    else:
        print("✗ Validation FAILED")
        print(f"\nFound {len(errors)} error(s):\n")
        for error in errors:
            print(f"  • {error}")
        return False

def validate_xbrl_references(checklist: dict) -> dict:
    """
    Analyze XBRL references in the checklist
    Returns summary of XBRL element usage
    """
    xbrl_usage = {}

    for section in checklist["audit_engagement"]["sections"]:
        for proc in section["procedures"]:
            if "xbrl_refs" in proc:
                for xbrl_ref in proc["xbrl_refs"]:
                    if xbrl_ref not in xbrl_usage:
                        xbrl_usage[xbrl_ref] = {
                            "count": 0,
                            "procedures": [],
                            "sections": set()
                        }
                    xbrl_usage[xbrl_ref]["count"] += 1
                    xbrl_usage[xbrl_ref]["procedures"].append(proc["procedure_id"])
                    xbrl_usage[xbrl_ref]["sections"].add(section["section_id"])

    return xbrl_usage

def print_xbrl_coverage_report(checklist: dict):
    """Print report of XBRL element coverage by audit procedures"""
    print("\n" + "="*60)
    print("XBRL ELEMENT COVERAGE REPORT")
    print("="*60)

    xbrl_usage = validate_xbrl_references(checklist)

    if not xbrl_usage:
        print("No XBRL references found in checklist")
        return

    print(f"\nTotal unique XBRL elements referenced: {len(xbrl_usage)}\n")

    for xbrl_element in sorted(xbrl_usage.keys()):
        usage = xbrl_usage[xbrl_element]
        print(f"\n{xbrl_element}")
        print(f"  Tested by {usage['count']} procedure(s): {', '.join(usage['procedures'])}")
        print(f"  Audit sections: {', '.join(sorted(usage['sections']))}")

    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    # First, create sample data if it doesn't exist
    try:
        with open("sample_audit_checklist.json", 'r') as f:
            pass
    except FileNotFoundError:
        print("Sample checklist not found. Creating it first...\n")
        import sys
        sys.path.append('..')
        from phase2_structured_data import audit_checklist_model
        audit_checklist_model.save_sample_checklist()
        print()

    # Validate the checklist
    filename = "sample_audit_checklist.json"
    success = load_and_validate_checklist(filename)

    if success:
        # Load and print XBRL coverage
        with open(filename, 'r', encoding='utf-8') as f:
            checklist = json.load(f)
        print_xbrl_coverage_report(checklist)

        print("\nValidation complete! Checklist is ready for:")
        print("  • Excel workpaper generation")
        print("  • XBRL cross-referencing")
        print("  • Progress tracking")
    else:
        print("\n✗ Please fix validation errors before proceeding")
        sys.exit(1)
