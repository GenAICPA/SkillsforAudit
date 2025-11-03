# Issue Title
🗺️ Roadmap: Phase 4 - Cross-Reference Engine

# Labels
enhancement, help wanted, phase-4

# Description

**Goal**: Build the cross-reference engine that links audit procedures → evidence documents → XBRL facts

## Overview

Phase 4 creates bidirectional relationships between three key components:
1. **Audit Procedures** (from JSON checklist)
2. **Evidence Documents** (workpaper references, file attachments)
3. **XBRL Facts** (financial statement data points)

This enables:
- ✅ Audit trail transparency (which procedures tested which financial statement items?)
- ✅ Coverage analysis (which XBRL elements are untested?)
- ✅ Evidence traceability (what evidence supports each financial statement assertion?)

## Requirements

### Core Functionality

**1. Cross-Reference Data Model**
```python
{
  "procedure_id": "REV-001",
  "xbrl_elements": ["us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax"],
  "evidence": [
    {
      "ref": "WP-A1",
      "type": "workpaper",
      "file_path": "evidence/revenue_sample.xlsx"
    }
  ],
  "assertions_tested": ["existence", "completeness", "accuracy"]
}
```

**2. Matching Algorithm**
- Parse `xbrl_refs` arrays from audit checklist procedures
- Match against parsed XBRL facts from Phase 3
- Identify procedures that test each XBRL element
- Flag XBRL elements with no testing coverage

**3. Coverage Analysis**
- Calculate % of XBRL elements tested
- Identify high-risk untested elements (materiality-based)
- Generate gap reports

**4. Traceability Reports**
- Audit trail showing: Assertion → Procedure → Evidence → XBRL Fact
- Export to Excel with hyperlinks between sheets
- Generate PDF documentation for audit files

## Proposed File Structure

```
phase4_cross_reference/
├── 10_cross_reference_engine.py     # Core mapping logic
├── 11_coverage_analysis.py           # Gap identification
├── 12_traceability_report.py         # Report generation
└── cross_reference_model.py          # Data structures
```

## Technical Considerations

**Input Sources:**
- Audit checklist JSON (from Phase 2)
- Parsed XBRL facts (from Phase 3)
- Evidence file registry (new)

**Output Formats:**
- Excel workbook (multiple sheets with cross-references)
- JSON (for programmatic use)
- PDF report (for audit documentation)

**Challenges:**
- Fuzzy matching (procedure descriptions vs XBRL element names)
- Multi-element procedures (one procedure tests multiple XBRL facts)
- Assertion mapping (which procedures test which assertions?)

## Help Wanted

We're looking for contributions in:
- 💻 **Algorithm design**: How to match procedures to XBRL elements
- 📊 **Data modeling**: Structure for cross-reference relationships
- 🎨 **Visualization**: How to display coverage gaps effectively
- 📝 **Documentation**: Explain the audit trail concept clearly

## Acceptance Criteria

- [ ] Data model supports bidirectional relationships
- [ ] Coverage analysis identifies untested XBRL elements
- [ ] Traceability report shows complete audit trail
- [ ] Works with existing Phase 2 and Phase 3 examples
- [ ] Generates professional Excel/PDF outputs
- [ ] Documented with clear examples

## References

- [PCAOB AS 1215](https://pcaobus.org/oversight/standards/auditing-standards/details/AS1215) - Audit Documentation
- [PCAOB AS 2810](https://pcaobus.org/oversight/standards/auditing-standards/details/AS2810) - Evaluating Audit Results
- See `AUDIT_SKILLS_ROADMAP.md` for detailed Phase 4 specifications

## Discussion

What approach would you take for matching procedures to XBRL elements? Please share ideas in the comments!

---

**Pin this issue** after creation to keep it visible
