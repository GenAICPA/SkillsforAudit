# Contributing to Skills for Audit

Thank you for your interest in contributing! This project aims to advance audit education and practice through AI-assisted workflows.

## How to Contribute

### For Accounting Educators

**Share Classroom Materials**
- Assignments or exercises you've created using these tools
- Student project examples (anonymized)
- Syllabi integrating Claude Skills into audit courses
- Assessment rubrics for AI-assisted audit work

**Provide Feedback**
- Which examples work well for teaching?
- What concepts need better explanation?
- Suggestions for additional phases or examples

### For Audit Practitioners

**Real-World Scenarios**
- Audit procedures from your methodology (anonymized)
- Common audit workflows that could benefit from automation
- Edge cases or complex scenarios
- Integration patterns with existing audit software

**Quality Standards**
- Mapping to PCAOB/AICPA/IAASB standards
- Firm quality control considerations
- Documentation requirements
- Review and sign-off workflows

### For Developers

**Code Contributions**
- Bug fixes
- Performance improvements
- New Skills integrations (PDF skill for audit reports)
- Additional XBRL parsing capabilities
- Cross-reference engine implementation (Phase 4)
- Integrated prototype (Phase 5)

**Testing**
- Unit tests for validation functions
- Integration tests for Skills API calls
- Test cases with edge scenarios
- XBRL samples from various industries

### For Regulators and Standard Setters

**Guidance**
- Regulatory considerations for AI-assisted audits
- Documentation requirements
- Audit trail standards
- Quality control frameworks

## Contribution Guidelines

### Code Standards

**Python Style**
- Follow PEP 8 style guide
- Use descriptive variable names (e.g., `audit_procedure` not `ap`)
- Add docstrings to all functions
- Include type hints where beneficial

**File Naming**
- Phase examples: `##_descriptive_name.py` (e.g., `07_parse_ixbrl_simple.py`)
- Utilities: `snake_case.py`
- Documentation: `UPPERCASE.md`

**Comments**
- Explain *why*, not *what*
- Reference audit standards (e.g., "Per AS 2201, test revenue cutoff")
- Link to XBRL taxonomy documentation where relevant

### Data Privacy and Anonymization

**CRITICAL: Never commit real client data**

Before contributing:
- ✅ Use fictional company names (e.g., "Example Corporation")
- ✅ Use synthetic financial data
- ✅ Anonymize all personally identifiable information
- ✅ Remove client-identifying metadata from files
- ❌ Never include actual engagement data
- ❌ Never include API keys or credentials

If you accidentally commit sensitive data:
1. Do NOT just delete the file in a new commit
2. Contact maintainers immediately
3. Use `git filter-branch` or BFG Repo-Cleaner to remove from history

### Submitting Contributions

**1. Fork and Clone**
```bash
git clone https://github.com/GenAICPA/SkillsforAudit.git
cd SkillsforAudit
```

**2. Create a Branch**
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

**3. Make Changes**
- Follow code standards above
- Test your changes locally
- Update documentation if needed

**4. Commit**
```bash
git add .
git commit -m "Brief description of changes

Longer explanation if needed:
- What changed
- Why it changed
- Any breaking changes or considerations"
```

**5. Push and Create Pull Request**
```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear title describing the change
- Description of what and why
- Screenshots if UI/output changes
- Reference any related issues

### Pull Request Review Process

1. **Automated Checks**: CI/CD tests must pass
2. **Code Review**: Maintainer reviews code quality and standards
3. **Content Review**: For audit content, verify accuracy and standards compliance
4. **Merge**: Once approved, maintainer merges to main branch

### Types of Contributions We're Looking For

**High Priority**
- [ ] Phase 4 cross-reference engine implementation
- [ ] Phase 5 integrated prototype
- [ ] Real-world XBRL samples (from SEC EDGAR)
- [ ] Additional validation rules for XBRL
- [ ] Test suite for existing examples

**Welcome Additions**
- [ ] PDF skill integration for audit reports
- [ ] Additional audit procedure examples (cash, investments, debt, equity)
- [ ] International standards examples (IAASB ISAs)
- [ ] Multi-language support
- [ ] Docker containerization

**Documentation Improvements**
- [ ] Video tutorials
- [ ] Screenshots of generated outputs
- [ ] Troubleshooting guides
- [ ] Translations

## Audit Content Guidelines

When contributing audit-related content:

**1. Reference Standards**
```python
"""
AS 2301: The Auditor's Responses to the Risks of Material Misstatement
This procedure tests management's assertions about revenue recognition.
"""
```

**2. Use Standard Terminology**
- Use professional audit terminology (not colloquial)
- Follow PCAOB/AICPA naming conventions
- Be consistent with existing examples

**3. Link to XBRL Taxonomy**
- Use correct US GAAP element names
- Include namespace (e.g., `us-gaap:Assets`)
- Link to taxonomy documentation: https://xbrl.us/home/filers/sec-reporting/

**4. Include Audit Assertions**
When documenting procedures, note which assertions are addressed:
- Existence/Occurrence
- Completeness
- Rights and Obligations
- Valuation/Allocation
- Presentation and Disclosure

## Testing Requirements

Before submitting code:

**1. Manual Testing**
```bash
# Test your specific example
python phase2_structured_data/your_new_example.py

# Verify it generates expected output
ls -l output_file.xlsx
```

**2. Validation Testing**
```bash
# If you modified validation logic
python phase2_structured_data/05_json_validation.py
```

**3. Integration Testing**
```bash
# Test end-to-end workflow
python phase2_structured_data/04_audit_checklist_model.py
python phase2_structured_data/05_json_validation.py
python phase2_structured_data/06_checklist_to_excel.py
```

## Getting Help

**Questions?**
- Open a [Discussion](https://github.com/GenAICPA/SkillsforAudit/discussions) for general questions
- Open an [Issue](https://github.com/GenAICPA/SkillsforAudit/issues) for bugs or specific problems
- Check existing issues/discussions first

**Want to Contribute But Don't Know Where to Start?**
- Look for issues labeled `good first issue`
- Check issues labeled `help wanted`
- Review `AUDIT_SKILLS_ROADMAP.md` for planned features

## Code of Conduct

### Our Standards

- **Professional**: Maintain audit profession's ethical standards
- **Respectful**: Value diverse perspectives (academic, practitioner, regulatory)
- **Constructive**: Focus on improving audit education and practice
- **Collaborative**: Work together toward common goals
- **Transparent**: Open about limitations and uncertainties with AI

### Unacceptable Behavior

- Sharing confidential client information
- Promoting misuse of AI to circumvent audit standards
- Harassment or discrimination
- Trolling or inflammatory comments
- Violation of professional ethics

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- Academic citations (for substantial content contributions)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Contact the maintainers or open a discussion on GitHub.

Thank you for helping advance audit education and practice!
