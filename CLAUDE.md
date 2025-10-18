# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository is a comprehensive learning path for applying Claude Skills to financial audit workflows. It progresses from basic document generation to sophisticated audit automation, including XBRL financial statement analysis and audit procedure cross-referencing.

The project is structured in 5 progressive phases, each building on previous concepts:
- **Phase 1**: Foundational Skills (PPTX, XLSX document generation)
- **Phase 2**: Structured audit data (JSON checklists, validation)
- **Phase 3**: XBRL parsing and validation
- **Phase 4**: Cross-reference engine (procedures ↔ evidence ↔ XBRL facts)
- **Phase 5**: Integrated prototype demonstration

Target audiences: accounting professors, US audit regulators, audit practitioners.

## Code Architecture

### Skills API Integration Pattern

All examples follow a consistent pattern for Skills API interaction:

1. **API Client Setup**: Initialize `anthropic.Anthropic()` client
2. **Beta Features**: Enable required betas: `code-execution-2025-08-25`, `skills-2025-10-02`, `files-api-2025-04-14`
3. **Container Configuration**: Specify skills in the container with `type: "anthropic"`, `skill_id` (e.g., "pptx", "xlsx"), and `version`
4. **Tool Configuration**: Include code_execution tool with type `code_execution_20250825`
5. **File Retrieval**: Extract `file_id` from response content blocks and download via `client.beta.files.retrieve_content(file_id)`

### Audit Data Model

The repository uses a structured JSON format for audit checklists:

```json
{
  "audit_engagement": {
    "client": "Example Corp",
    "period_end": "2024-12-31",
    "sections": [
      {
        "section_id": "AS.2201",
        "name": "Revenue Recognition",
        "risk_level": "high",
        "procedures": [
          {
            "procedure_id": "REV-001",
            "description": "Test sales cutoff",
            "status": "completed",
            "evidence_refs": ["WP-A1"],
            "xbrl_refs": ["us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax"],
            "sign_off": {
              "auditor": "Emily Rodriguez, CPA",
              "date": "2025-02-15"
            }
          }
        ]
      }
    ]
  }
}
```

**Key fields**:
- `status`: not_started, in_progress, completed, not_applicable
- `evidence_refs`: Links to workpaper references or document IDs
- `xbrl_refs`: XBRL element names from US GAAP taxonomy
- `sign_off`: Auditor accountability (required when status=completed)

### XBRL Integration

The repository includes examples for parsing Inline XBRL (iXBRL) financial statements:
- Extract facts (ix:nonFraction elements) with element name, value, context, unit
- Validate mathematical relationships (e.g., Assets = Liabilities + Equity)
- Calculate financial ratios from XBRL data
- Cross-reference XBRL elements to audit procedures

### Cross-Reference Architecture

The planned cross-reference engine (Phase 4) creates bidirectional links:
- **Audit Procedure** → **Evidence Documents** → **XBRL Facts**
- Enables coverage analysis: which XBRL elements are tested?
- Generates traceability reports for regulatory compliance

### Original Test Scripts

The root directory contains original test scripts:
- **test-skills.py**: Debug version that inspects response structure
- **test-skills-download.py**: File extraction with error handling
- **simple-skills-download.py**: Minimal implementation

These demonstrate the basic API pattern before applying it to audit use cases.

## Development Commands

### Phase 1: Basic Skills

```bash
cd phase1_foundations

# Generate audit engagement presentation (PPTX)
python 01_basic_pptx.py

# Generate bank reconciliation workpaper (XLSX)
python 02_basic_xlsx.py

# Calculate audit samples with code execution (XLSX)
python 03_code_execution_pattern.py
```

### Phase 2: Structured Data

```bash
cd phase2_structured_data

# Create audit checklist JSON schema and sample data
python 04_audit_checklist_model.py

# Validate checklist structure and XBRL references
python 05_json_validation.py

# Generate Excel workpaper from checklist JSON
python 06_checklist_to_excel.py
```

### Phase 3: XBRL

```bash
cd phase3_xbrl

# Parse Inline XBRL and generate audit analysis workpaper
python 07_parse_ixbrl_simple.py
```

### Original Test Scripts

```bash
# Basic Skills API testing (root directory)
python test-skills.py                  # Debug response structure
python test-skills-download.py         # File download with error handling
python simple-skills-download.py       # Minimal implementation
```

### Running All Examples Sequentially

```bash
# From repository root, run all phases in order
python phase1_foundations/01_basic_pptx.py
python phase1_foundations/02_basic_xlsx.py
python phase2_structured_data/04_audit_checklist_model.py
python phase2_structured_data/05_json_validation.py
python phase2_structured_data/06_checklist_to_excel.py
python phase3_xbrl/07_parse_ixbrl_simple.py
```

## Environment Requirements

- **Python**: 3.13+ (tested with Python 3.13.7)
- **Package**: `anthropic` Python SDK (`pip install anthropic`)
- **API Key**: Valid Anthropic API key (set as `ANTHROPIC_API_KEY` environment variable)
- **Model**: Uses `claude-haiku-4-5-20251001` for cost-effective learning
- **Token Range**: 2048-4096 max_tokens depending on task complexity

## Key Implementation Patterns

### Pattern 1: Simple Document Generation
```python
# Generate a document from a text prompt
response = client.beta.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=2048,
    betas=["code-execution-2025-08-25", "skills-2025-10-02", "files-api-2025-04-14"],
    container={"skills": [{"type": "anthropic", "skill_id": "pptx", "version": "latest"}]},
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    messages=[{"role": "user", "content": "Create a presentation about..."}]
)
```

### Pattern 2: Data-Driven Document Generation
```python
# Load structured data, build prompt, generate document
with open('sample_audit_checklist.json', 'r') as f:
    checklist = json.load(f)

prompt = f"Create Excel workpaper with data: {json.dumps(checklist)}"
response = client.beta.messages.create(...)  # Same API pattern
```

### Pattern 3: Code Execution + Skills
```python
# Claude uses code execution to process data, then generates document
# Example: Parse XBRL → Validate → Generate Excel analysis
response = client.beta.messages.create(
    # ... same config ...
    messages=[{
        "role": "user",
        "content": "Parse this XBRL file, validate it, then create an Excel workpaper..."
    }]
)
```

## File Naming Conventions

- **Generated files**: Descriptive names based on content (e.g., `audit_engagement_presentation.pptx`)
- **Sample data**: Prefix with `sample_` (e.g., `sample_audit_checklist.json`)
- **Schema files**: Suffix with `_schema` (e.g., `audit_checklist_schema.json`)
- **Workpaper references**: Use standard audit notation (e.g., `A-1`, `B-2`, `C-3`)

## Notes for Future Development

- **Phase 4** (Cross-reference engine): Will need to map `xbrl_refs` arrays in procedures to parsed XBRL facts
- **Phase 5** (Prototype): Should integrate all components into a single workflow with command-line interface
- **XBRL taxonomy**: Currently uses US GAAP element names (prefix: `us-gaap:`)
- **Audit standards**: Examples reference PCAOB auditing standards (e.g., AS.2201 for Revenue Recognition)
- **File outputs**: All generated files saved to current working directory; consider organizing by phase in production
