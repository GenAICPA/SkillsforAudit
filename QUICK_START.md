# Quick Start Guide - Claude Skills for Audit

Get started with Claude Skills for financial audit in 15 minutes.

## Setup (2 minutes)

```bash
# 1. Install Python package
pip install anthropic

# 2. Set API key (Windows)
set ANTHROPIC_API_KEY=your-api-key-here

# 3. Verify installation
python -c "import anthropic; print('Ready!')"
```

## Your First Example (5 minutes)

### Generate an Audit Presentation

```bash
cd phase1_foundations
python 01_basic_pptx.py
```

**What it does**: Creates a professional PowerPoint presentation for an audit engagement kickoff

**Output**: `audit_engagement_presentation.pptx`

**Learn**: Basic Skills API pattern (PPTX skill)

### Generate an Excel Workpaper

```bash
python 02_basic_xlsx.py
```

**What it does**: Creates a bank reconciliation workpaper in Excel with formulas and formatting

**Output**: `bank_reconciliation_workpaper.xlsx`

**Learn**: XLSX skill with professional audit formatting

## Understanding the Data Model (5 minutes)

### Create Audit Checklist

```bash
cd ../phase2_structured_data
python 04_audit_checklist_model.py
```

**What it creates**:
- `sample_audit_checklist.json` - Example audit program structure
- `audit_checklist_schema.json` - JSON schema for validation

**What you'll see**: Structured audit procedures with:
- Status tracking (not_started, in_progress, completed)
- XBRL references linking to financial statement elements
- Evidence references for documentation
- Auditor sign-offs

### Validate and Generate

```bash
# Validate the checklist structure
python 05_json_validation.py

# Generate Excel workpaper from the checklist
python 06_checklist_to_excel.py
```

**Output**: `audit_program_Example_Corporation.xlsx` - A multi-sheet workpaper with:
- Audit Summary
- Procedure details by section (Revenue, Inventory, etc.)
- XBRL cross-reference mapping

## XBRL Financial Statement Analysis (3 minutes)

```bash
cd ../phase3_xbrl
python 07_parse_ixbrl_simple.py
```

**What it does**:
1. Creates a sample Inline XBRL financial statement
2. Parses and extracts all XBRL facts using code execution
3. Validates mathematical relationships (Assets = Liabilities + Equity)
4. Calculates financial ratios
5. Generates an Excel audit analysis workpaper

**Outputs**:
- `sample_ixbrl_financials.html` - Sample Inline XBRL document
- `xbrl_audit_analysis.xlsx` - Excel analysis with validation and ratios

## Key Concepts

### 1. Skills API Pattern

Every example follows this structure:

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=4096,

    # Enable required beta features
    betas=["code-execution-2025-08-25", "skills-2025-10-02", "files-api-2025-04-14"],

    # Specify which skill to use
    container={
        "skills": [
            {
                "type": "anthropic",
                "skill_id": "xlsx",  # or "pptx", "pdf"
                "version": "latest"
            }
        ]
    },

    # Enable code execution
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],

    # Your prompt
    messages=[{"role": "user", "content": "Create a workpaper..."}]
)

# Download generated file
for block in response.content:
    if hasattr(block, 'file_id') and block.file_id:
        file_content = client.beta.files.retrieve_content(block.file_id)
        with open('output.xlsx', 'wb') as f:
            f.write(file_content)
```

### 2. Audit Data Structure

Checklists use this JSON structure:

```json
{
  "audit_engagement": {
    "client": "Example Corp",
    "sections": [
      {
        "section_id": "AS.2201",
        "name": "Revenue Recognition",
        "procedures": [
          {
            "procedure_id": "REV-001",
            "status": "completed",
            "xbrl_refs": ["us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax"],
            "evidence_refs": ["WP-A1"]
          }
        ]
      }
    ]
  }
}
```

### 3. XBRL Integration

Inline XBRL embeds structured data in HTML:

```html
<td>$<ix:nonFraction
    name="us-gaap:Assets"
    contextRef="AsOf_2024-12-31"
    unitRef="USD"
    decimals="-3">13132000</ix:nonFraction></td>
```

Parse it with Claude to:
- Extract financial facts
- Validate relationships
- Cross-reference with audit procedures
- Calculate ratios

## What's Next?

### For Learning
1. **Modify examples**: Change client names, add procedures, adjust risk levels
2. **Combine phases**: Load checklist → validate → generate workpaper → parse XBRL
3. **Real data**: Download actual Inline XBRL from SEC EDGAR database

### For Teaching (Professors)
- Use Phase 1 examples for intro to AI in audit (Week 1-2)
- Phase 2 for audit data structures and automation (Week 3-4)
- Phase 3 for XBRL and modern financial reporting (Week 5-6)
- Phases 4-5 for capstone project: build complete audit assistant

### For Regulators
- Review `AUDIT_SKILLS_ROADMAP.md` for compliance considerations
- Focus on audit trail transparency (sign-offs, evidence links)
- Test validation logic (mathematical checks, schema validation)
- Evaluate explainability of AI-generated analyses

### For Practitioners
- Adapt templates to your firm's methodology
- Integrate with existing audit software
- Build custom skills for specialized procedures
- Scale to multiple engagements

## Common Issues

### "No module named 'anthropic'"
```bash
pip install anthropic
```

### "API key not found"
```bash
# Windows
set ANTHROPIC_API_KEY=your-key

# Linux/Mac
export ANTHROPIC_API_KEY=your-key
```

### "File not found: sample_audit_checklist.json"
```bash
# Create sample data first
python 04_audit_checklist_model.py
```

### "No file_id in response"
- Check if Skills beta is enabled in your API key settings
- Verify beta strings are correct in code
- Ensure max_tokens is sufficient (>2048 for complex documents)

## Resources

- **Full Documentation**: See `README.md`
- **Learning Roadmap**: See `AUDIT_SKILLS_ROADMAP.md`
- **Code Reference**: See `CLAUDE.md` (for Claude Code users)
- **Anthropic Docs**: https://docs.anthropic.com

## Getting Help

1. Review error messages carefully (Claude provides detailed feedback)
2. Check `CLAUDE.md` for implementation patterns
3. Examine working examples in each phase directory
4. Simplify your prompt and add complexity gradually

## Time Investment

- **Quick exploration**: 15 minutes (this guide)
- **Phase 1 mastery**: 2-4 hours (practice each example)
- **Phase 2 mastery**: 4-6 hours (understand data modeling)
- **Phase 3 mastery**: 4-6 hours (XBRL deep dive)
- **Complete learning path**: 20-30 hours (all phases + custom projects)

## Success Metrics

You'll know you're ready to move forward when you can:

✅ Generate audit documents (PPTX, XLSX) from prompts
✅ Create and validate structured audit data (JSON)
✅ Transform data into formatted workpapers automatically
✅ Parse XBRL financial statements and extract facts
✅ Understand how to link procedures ↔ evidence ↔ XBRL

Good luck! Start with Phase 1 and work sequentially.
