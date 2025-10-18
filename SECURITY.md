# Security Policy

## Supported Versions

This is an educational project under active development. Security updates are provided for the latest version on the main branch.

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |
| other   | :x:                |

## Security Considerations

### Data Privacy

**CRITICAL**: This toolkit processes financial data and audit information. Users must:

1. **Never commit real client data** to this repository
2. **Use only fictional or anonymized data** in examples
3. **Protect API keys** - never commit `.env` files or hardcode keys
4. **Review generated files** before sharing to ensure no sensitive data leakage

### API Key Security

The project uses Anthropic's Claude API which requires an API key:

**✅ Secure practices:**
- Store API key in environment variable (`ANTHROPIC_API_KEY`)
- Use `.env` file (excluded by `.gitignore`)
- Rotate keys regularly
- Use separate keys for development/production

**❌ Insecure practices:**
- Hardcoding keys in source code
- Committing keys to version control
- Sharing keys in screenshots or documentation
- Using production keys for testing

### Audit Data Handling

When using this toolkit for educational purposes:

1. **Generate synthetic data**: Use fictional companies and amounts
2. **Anonymize real examples**: Remove all identifying information
3. **Review outputs**: Ensure AI-generated content doesn't expose patterns from training data
4. **Secure storage**: Generated workpapers may contain sensitive prompts or data
5. **Disposal**: Securely delete generated files when no longer needed

### XBRL Data Sources

When working with XBRL financial statements:

- **Public filings**: SEC EDGAR data is public and safe to use
- **Private companies**: Obtain explicit permission before using real data
- **Test data**: Use the provided sample XBRL files for learning
- **Attribution**: Credit sources when using real-world examples

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability:

### What to Report

**Report these issues:**
- API key exposure in code or commits
- Data leakage in generated files
- Injection vulnerabilities in prompts
- Unauthorized data access
- Dependency vulnerabilities

**Don't report these (not security issues):**
- Bugs in example code
- Feature requests
- Documentation issues

### How to Report

**For sensitive security issues:**

1. **Do NOT open a public GitHub issue**
2. Email: [Create a private security advisory on GitHub]
   - Go to: https://github.com/GenAICPA/SkillsforAudit/security/advisories/new
   - Or email maintainers directly (contact info in GitHub profile)
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

**Response timeline:**
- Initial response: Within 48 hours
- Status update: Within 7 days
- Fix timeline: Depends on severity (critical issues prioritized)

### What Happens Next

1. **Acknowledgment**: We'll confirm receipt and assess severity
2. **Investigation**: We'll investigate and develop a fix
3. **Disclosure**: We'll coordinate disclosure timing with you
4. **Credit**: We'll credit you in the fix announcement (unless you prefer anonymity)
5. **Update**: We'll update this security policy if needed

## Security Best Practices for Users

### For Developers

```python
# ✅ Good: Use environment variables
import os
api_key = os.getenv('ANTHROPIC_API_KEY')

# ❌ Bad: Hardcoded key
api_key = 'sk-ant-...'  # NEVER DO THIS
```

### For Educators

1. **Sanitize examples**: Remove all real client data before sharing with students
2. **Key management**: Provide guidance on API key security to students
3. **Monitoring**: If providing shared API keys, monitor usage for abuse
4. **Policies**: Establish acceptable use policies for AI tools

### For Practitioners

1. **Separation**: Never use this toolkit with real client data without explicit controls
2. **Compliance**: Ensure use complies with firm policies and professional standards
3. **Review**: Have security team review before using in production
4. **Documentation**: Document all AI tool usage per audit standards

## Dependencies

This project uses third-party packages. Security considerations:

- **Anthropic SDK**: Official package, regularly updated
- **Python standard library**: Follow Python security advisories
- **Future additions**: Review dependencies before adding

### Checking for Vulnerabilities

```bash
# Check for known vulnerabilities
pip install safety
safety check

# Or use pip-audit
pip install pip-audit
pip-audit
```

## Compliance Considerations

### Professional Standards

Users must ensure compliance with:
- **PCAOB**: Rules on audit documentation and quality control
- **AICPA**: Professional standards and ethics
- **Firm policies**: Individual firm quality control standards
- **Data protection**: GDPR, CCPA, or applicable regulations

### AI Ethics

When using AI in audit contexts:
- Maintain professional skepticism
- Don't rely solely on AI outputs
- Document AI tool usage appropriately
- Ensure human oversight of judgments
- Protect client confidentiality

## Incident Response

If you accidentally commit sensitive data:

### Immediate Actions

1. **Stop**: Don't make additional commits
2. **Report**: Contact maintainers immediately via security advisory
3. **Document**: Note what was exposed and when
4. **Notify**: Inform affected parties if real client data was exposed

### Remediation

We will:
1. Remove sensitive data from git history (using BFG Repo-Cleaner or similar)
2. Rotate any exposed API keys
3. Assess impact and notify affected parties
4. Update security controls to prevent recurrence

## Questions?

For non-sensitive security questions:
- Open a [Discussion](https://github.com/GenAICPA/SkillsforAudit/discussions)
- Review [CONTRIBUTING.md](CONTRIBUTING.md) for data privacy guidelines

For sensitive issues:
- Use GitHub Security Advisory (preferred)
- Contact maintainers privately

## Updates to This Policy

This security policy may be updated as the project evolves. Check back regularly for changes.

Last updated: 2025-10-18
