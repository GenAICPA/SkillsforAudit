# Issue Title
📚 Wanted: Real-World XBRL Examples from SEC EDGAR

# Labels
help wanted, data, xbrl, good first contribution

# Description

We're looking for **real-world Inline XBRL filings** from the SEC EDGAR database to test and enhance Phase 3 parsing capabilities.

## Why This Matters

The current Phase 3 example uses a simplified, hand-crafted Inline XBRL file. Real SEC filings are:
- More complex (multiple contexts, dimensions, taxonomies)
- Larger scale (thousands of facts vs. dozens)
- Varied formats (different rendering styles)
- Include edge cases (corrections, restatements, complex transactions)

Testing with real filings ensures our educational materials reflect actual audit scenarios.

## What We Need

### Priority 1: Diverse Industries

One example from each:
- [ ] **Technology** (e.g., Microsoft, Apple, Adobe)
- [ ] **Manufacturing** (e.g., General Motors, 3M, Caterpillar)
- [ ] **Retail** (e.g., Walmart, Target, Amazon)
- [ ] **Financial Services** (e.g., JPMorgan, Bank of America - note: different XBRL extensions)
- [ ] **Healthcare** (e.g., Johnson & Johnson, Pfizer)

### Priority 2: Company Sizes

- [ ] **Large cap** ($10B+ market cap)
- [ ] **Mid cap** ($2B-$10B market cap)
- [ ] **Small cap** (<$2B market cap)

### Priority 3: Complex Scenarios

- [ ] Mergers & acquisitions (segment reporting)
- [ ] Discontinued operations
- [ ] Foreign currency translation
- [ ] Multi-segment businesses
- [ ] Restatements or corrections

## How to Contribute

### Option 1: Share a Link

1. Go to [SEC EDGAR Company Search](https://www.sec.gov/edgar/searchedgar/companysearch.html)
2. Find a company you're interested in
3. Look for their latest **10-K** or **10-Q** filing
4. Find the "Financial Statements" exhibit (usually labeled with "EX-101")
5. Copy the link to the Inline XBRL file (ends in `.htm` or `.html`)
6. Post it in the comments below with:
   - Company name
   - Fiscal year/quarter
   - Why it's interesting (industry, complexity, etc.)

**Example:**
```
Company: Apple Inc. (AAPL)
Filing: 10-K for fiscal year 2023
Link: [paste EDGAR link]
Why: Large tech company, segment reporting, international operations
```

### Option 2: Submit via Pull Request

If you'd like to add the file directly:

1. Download the Inline XBRL file from EDGAR
2. Anonymize/simplify if desired (optional)
3. Add to `sample_data/sample_ixbrl/[company_name]/`
4. Include a README.md with:
   - Company name and ticker
   - Filing type and period
   - Source URL (EDGAR link)
   - Any notable features

Example structure:
```
sample_data/sample_ixbrl/
├── apple_10k_2023/
│   ├── financial_statements.html
│   ├── README.md
│   └── notes.txt
```

### Option 3: Just Tell Us the CIK

If you don't want to navigate EDGAR, just share the company's **CIK number**:
- Company: Apple Inc.
- CIK: 0000320193

We'll find and download the appropriate filing.

## What Happens Next?

Once we have real XBRL examples:
1. **Enhance Phase 3** parser to handle real-world complexity
2. **Create test cases** for different scenarios
3. **Build industry-specific examples** (tech audit vs. retail audit)
4. **Improve error handling** for malformed XBRL
5. **Develop advanced analytics** (segment analysis, trend detection)

## Legal/Data Considerations

✅ **All SEC EDGAR data is public domain** - no copyright issues
✅ **No PII** - financial statements don't contain personal information
✅ **Attribution** - we'll credit contributors in documentation

## Examples Already Available

These companies have good Inline XBRL filings:
- Microsoft (CIK: 0000789019) - Clean, well-structured
- Starbucks (CIK: 0000829224) - Retail operations
- Boeing (CIK: 0000012927) - Manufacturing, complex contracts

## Questions?

- **Q: Do I need to understand XBRL?**
  A: No! Just share the link. We'll handle the technical details.

- **Q: Should I test the parsing first?**
  A: Not required, but if you want to, run Phase 3 on it and share results!

- **Q: Can I suggest a non-US company?**
  A: For now, we're focusing on US GAAP (SEC EDGAR). IFRS support may come later.

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Credited in the Phase 3 documentation
- Acknowledged in any published materials using the examples

---

**Thank you for helping make this educational resource more realistic and valuable!** 🙏

Drop links in the comments below or open a PR with your examples!
