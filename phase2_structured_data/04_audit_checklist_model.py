"""
Phase 2, Example 4: Audit Checklist Data Model
Purpose: Define structured data models for audit checklists
Scenario: Create JSON schemas and sample data for audit procedures
"""

import json
from datetime import datetime
from typing import List, Optional, Dict

# Define the audit checklist data structure
AUDIT_CHECKLIST_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Audit Checklist",
    "type": "object",
    "required": ["audit_engagement", "version"],
    "properties": {
        "version": {"type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$"},
        "audit_engagement": {
            "type": "object",
            "required": ["client", "period_end", "engagement_partner", "sections"],
            "properties": {
                "client": {"type": "string"},
                "client_id": {"type": "string"},
                "period_end": {"type": "string", "format": "date"},
                "fiscal_year": {"type": "integer"},
                "engagement_partner": {"type": "string"},
                "materiality": {"type": "number"},
                "sections": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["section_id", "name", "procedures"],
                        "properties": {
                            "section_id": {"type": "string"},
                            "name": {"type": "string"},
                            "description": {"type": "string"},
                            "risk_level": {"enum": ["low", "medium", "high"]},
                            "procedures": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "required": ["procedure_id", "description", "status"],
                                    "properties": {
                                        "procedure_id": {"type": "string"},
                                        "description": {"type": "string"},
                                        "status": {
                                            "enum": ["not_started", "in_progress", "completed", "not_applicable"]
                                        },
                                        "assigned_to": {"type": "string"},
                                        "due_date": {"type": "string", "format": "date"},
                                        "evidence_refs": {
                                            "type": "array",
                                            "items": {"type": "string"}
                                        },
                                        "xbrl_refs": {
                                            "type": "array",
                                            "items": {"type": "string"}
                                        },
                                        "workpaper_ref": {"type": "string"},
                                        "sign_off": {
                                            "type": "object",
                                            "properties": {
                                                "auditor": {"type": "string"},
                                                "date": {"type": "string", "format": "date"},
                                                "notes": {"type": "string"},
                                                "exceptions": {"type": "boolean"}
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

# Sample audit checklist data
SAMPLE_CHECKLIST = {
    "version": "1.0.0",
    "audit_engagement": {
        "client": "Example Corporation",
        "client_id": "EXM-001",
        "period_end": "2024-12-31",
        "fiscal_year": 2024,
        "engagement_partner": "Sarah Johnson, CPA",
        "materiality": 500000,
        "sections": [
            {
                "section_id": "AS.2201",
                "name": "Revenue Recognition",
                "description": "Audit procedures for revenue recognition under ASC 606",
                "risk_level": "high",
                "procedures": [
                    {
                        "procedure_id": "REV-001",
                        "description": "Test sales transactions for proper cutoff at year-end",
                        "status": "completed",
                        "assigned_to": "Emily Rodriguez",
                        "due_date": "2025-02-15",
                        "evidence_refs": ["WP-A1", "WP-A2", "DOC-Sales-Sample"],
                        "xbrl_refs": ["us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax"],
                        "workpaper_ref": "A-1",
                        "sign_off": {
                            "auditor": "Emily Rodriguez, CPA",
                            "date": "2025-02-15",
                            "notes": "Tested 40 transactions around year-end. No exceptions noted.",
                            "exceptions": False
                        }
                    },
                    {
                        "procedure_id": "REV-002",
                        "description": "Verify revenue recognition timing complies with ASC 606 performance obligations",
                        "status": "in_progress",
                        "assigned_to": "James Lee",
                        "due_date": "2025-02-20",
                        "evidence_refs": ["WP-A3"],
                        "xbrl_refs": ["us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax", "us-gaap:ContractWithCustomerAssetNet"],
                        "workpaper_ref": "A-2"
                    },
                    {
                        "procedure_id": "REV-003",
                        "description": "Test accounts receivable aging and collectibility",
                        "status": "not_started",
                        "assigned_to": "David Park",
                        "due_date": "2025-02-25",
                        "evidence_refs": [],
                        "xbrl_refs": ["us-gaap:AccountsReceivableNetCurrent", "us-gaap:AllowanceForDoubtfulAccountsReceivableCurrent"],
                        "workpaper_ref": "A-3"
                    }
                ]
            },
            {
                "section_id": "AS.2501",
                "name": "Inventory",
                "description": "Audit procedures for inventory valuation and existence",
                "risk_level": "medium",
                "procedures": [
                    {
                        "procedure_id": "INV-001",
                        "description": "Perform physical inventory observation",
                        "status": "completed",
                        "assigned_to": "Emily Rodriguez",
                        "due_date": "2025-01-05",
                        "evidence_refs": ["WP-B1", "PHOTO-Inventory-Count"],
                        "xbrl_refs": ["us-gaap:InventoryNet"],
                        "workpaper_ref": "B-1",
                        "sign_off": {
                            "auditor": "Emily Rodriguez, CPA",
                            "date": "2025-01-05",
                            "notes": "Observed count on 1/5/2025. Client count procedures adequate. Test counts agreed to client counts.",
                            "exceptions": False
                        }
                    },
                    {
                        "procedure_id": "INV-002",
                        "description": "Test lower of cost or net realizable value",
                        "status": "completed",
                        "assigned_to": "James Lee",
                        "due_date": "2025-02-10",
                        "evidence_refs": ["WP-B2", "DATA-Pricing"],
                        "xbrl_refs": ["us-gaap:InventoryNet", "us-gaap:InventoryValuationReserves"],
                        "workpaper_ref": "B-2",
                        "sign_off": {
                            "auditor": "James Lee, CPA",
                            "date": "2025-02-10",
                            "notes": "Reviewed slow-moving and obsolete inventory. Client reserves appear adequate.",
                            "exceptions": False
                        }
                    }
                ]
            },
            {
                "section_id": "AS.2401",
                "name": "Related Party Transactions",
                "description": "Identification and disclosure of related party transactions",
                "risk_level": "medium",
                "procedures": [
                    {
                        "procedure_id": "RPT-001",
                        "description": "Obtain list of related parties from management",
                        "status": "completed",
                        "assigned_to": "Michael Chen",
                        "due_date": "2025-01-30",
                        "evidence_refs": ["DOC-Related-Party-List"],
                        "xbrl_refs": ["us-gaap:RelatedPartyTransactionsByRelatedPartyAxis"],
                        "workpaper_ref": "F-1",
                        "sign_off": {
                            "auditor": "Michael Chen, CPA",
                            "date": "2025-01-30",
                            "notes": "Obtained and documented related party list.",
                            "exceptions": False
                        }
                    },
                    {
                        "procedure_id": "RPT-002",
                        "description": "Review significant transactions for related party involvement",
                        "status": "not_started",
                        "assigned_to": "Michael Chen",
                        "due_date": "2025-02-28",
                        "evidence_refs": [],
                        "xbrl_refs": ["us-gaap:RelatedPartyTransactionAmountsOfTransaction"],
                        "workpaper_ref": "F-2"
                    }
                ]
            }
        ]
    }
}

def save_sample_checklist():
    """Save sample checklist to JSON file"""
    output_file = "sample_audit_checklist.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(SAMPLE_CHECKLIST, f, indent=2)
    print(f"✓ Sample checklist saved to: {output_file}")
    return output_file

def save_schema():
    """Save JSON schema to file"""
    output_file = "audit_checklist_schema.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(AUDIT_CHECKLIST_SCHEMA, f, indent=2)
    print(f"✓ Schema saved to: {output_file}")
    return output_file

def print_checklist_summary(checklist: dict):
    """Print a summary of the audit checklist"""
    engagement = checklist["audit_engagement"]

    print("\n" + "="*60)
    print(f"AUDIT CHECKLIST SUMMARY")
    print("="*60)
    print(f"Client: {engagement['client']}")
    print(f"Period End: {engagement['period_end']}")
    print(f"Engagement Partner: {engagement['engagement_partner']}")
    print(f"Materiality: ${engagement['materiality']:,}")
    print("="*60)

    total_procedures = 0
    completed_procedures = 0

    for section in engagement["sections"]:
        print(f"\n{section['section_id']}: {section['name']}")
        print(f"  Risk Level: {section['risk_level'].upper()}")
        print(f"  Procedures:")

        for proc in section["procedures"]:
            total_procedures += 1
            status_icon = "✓" if proc["status"] == "completed" else "○"
            if proc["status"] == "completed":
                completed_procedures += 1

            print(f"    {status_icon} {proc['procedure_id']}: {proc['description'][:60]}...")
            print(f"      Status: {proc['status']} | Assigned: {proc.get('assigned_to', 'Unassigned')}")

            if proc.get('xbrl_refs'):
                print(f"      XBRL Links: {', '.join(proc['xbrl_refs'][:2])}...")

    print("\n" + "="*60)
    print(f"COMPLETION: {completed_procedures}/{total_procedures} procedures completed")
    print(f"PROGRESS: {(completed_procedures/total_procedures*100):.1f}%")
    print("="*60 + "\n")

if __name__ == "__main__":
    print("Creating audit checklist data model and sample data...\n")

    # Save files
    schema_file = save_schema()
    checklist_file = save_sample_checklist()

    # Print summary
    print_checklist_summary(SAMPLE_CHECKLIST)

    print("\nNext steps:")
    print("1. Use this checklist structure for all audit programs")
    print("2. Validate checklist files against the schema (see next example)")
    print("3. Generate Excel workpapers from this data (see example 06)")
