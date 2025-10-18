"""
Phase 3, Example 7: Parse Inline XBRL (Simplified)
Purpose: Extract financial data from Inline XBRL documents
Scenario: Read XBRL facts from a simplified financial statement
"""

import anthropic
import json

def create_sample_ixbrl():
    """Create a simplified Inline XBRL document for demonstration"""
    ixbrl_content = """<!DOCTYPE html>
<html xmlns:ix="http://www.xbrl.org/2013/inlineXBRL"
      xmlns:xbrli="http://www.xbrl.org/2003/instance"
      xmlns:us-gaap="http://fasb.org/us-gaap/2024">
<head>
    <title>Example Corporation - Financial Statements</title>
</head>
<body>
    <h1>Example Corporation</h1>
    <h2>Balance Sheet (Unaudited)</h2>
    <p>As of <ix:nonFraction name="us-gaap:BalanceSheetDate" contextRef="AsOf_2024-12-31" format="date">December 31, 2024</ix:nonFraction></p>

    <table>
        <tr>
            <th>Assets</th>
            <th>Amount</th>
        </tr>
        <tr>
            <td>Cash and Cash Equivalents</td>
            <td>$<ix:nonFraction name="us-gaap:CashAndCashEquivalentsAtCarryingValue" contextRef="AsOf_2024-12-31" unitRef="USD" decimals="-3">1245000</ix:nonFraction></td>
        </tr>
        <tr>
            <td>Accounts Receivable, Net</td>
            <td>$<ix:nonFraction name="us-gaap:AccountsReceivableNetCurrent" contextRef="AsOf_2024-12-31" unitRef="USD" decimals="-3">3567000</ix:nonFraction></td>
        </tr>
        <tr>
            <td>Inventory</td>
            <td>$<ix:nonFraction name="us-gaap:InventoryNet" contextRef="AsOf_2024-12-31" unitRef="USD" decimals="-3">2890000</ix:nonFraction></td>
        </tr>
        <tr>
            <td><strong>Total Current Assets</strong></td>
            <td><strong>$<ix:nonFraction name="us-gaap:AssetsCurrent" contextRef="AsOf_2024-12-31" unitRef="USD" decimals="-3">7702000</ix:nonFraction></strong></td>
        </tr>
        <tr>
            <td>Property, Plant and Equipment, Net</td>
            <td>$<ix:nonFraction name="us-gaap:PropertyPlantAndEquipmentNet" contextRef="AsOf_2024-12-31" unitRef="USD" decimals="-3">5430000</ix:nonFraction></td>
        </tr>
        <tr>
            <td><strong>Total Assets</strong></td>
            <td><strong>$<ix:nonFraction name="us-gaap:Assets" contextRef="AsOf_2024-12-31" unitRef="USD" decimals="-3">13132000</ix:nonFraction></strong></td>
        </tr>
    </table>

    <table>
        <tr>
            <th>Liabilities and Equity</th>
            <th>Amount</th>
        </tr>
        <tr>
            <td>Accounts Payable</td>
            <td>$<ix:nonFraction name="us-gaap:AccountsPayableCurrent" contextRef="AsOf_2024-12-31" unitRef="USD" decimals="-3">1560000</ix:nonFraction></td>
        </tr>
        <tr>
            <td>Accrued Liabilities</td>
            <td>$<ix:nonFraction name="us-gaap:AccruedLiabilitiesCurrent" contextRef="AsOf_2024-12-31" unitRef="USD" decimals="-3">890000</ix:nonFraction></td>
        </tr>
        <tr>
            <td><strong>Total Current Liabilities</strong></td>
            <td><strong>$<ix:nonFraction name="us-gaap:LiabilitiesCurrent" contextRef="AsOf_2024-12-31" unitRef="USD" decimals="-3">2450000</ix:nonFraction></strong></td>
        </tr>
        <tr>
            <td>Long-term Debt</td>
            <td>$<ix:nonFraction name="us-gaap:LongTermDebt" contextRef="AsOf_2024-12-31" unitRef="USD" decimals="-3">3200000</ix:nonFraction></td>
        </tr>
        <tr>
            <td><strong>Total Liabilities</strong></td>
            <td><strong>$<ix:nonFraction name="us-gaap:Liabilities" contextRef="AsOf_2024-12-31" unitRef="USD" decimals="-3">5650000</ix:nonFraction></strong></td>
        </tr>
        <tr>
            <td>Stockholders' Equity</td>
            <td>$<ix:nonFraction name="us-gaap:StockholdersEquity" contextRef="AsOf_2024-12-31" unitRef="USD" decimals="-3">7482000</ix:nonFraction></td>
        </tr>
        <tr>
            <td><strong>Total Liabilities and Equity</strong></td>
            <td><strong>$<ix:nonFraction name="us-gaap:LiabilitiesAndStockholdersEquity" contextRef="AsOf_2024-12-31" unitRef="USD" decimals="-3">13132000</ix:nonFraction></strong></td>
        </tr>
    </table>

    <h2>Income Statement (Unaudited)</h2>
    <p>For the Year Ended <ix:nonFraction name="us-gaap:IncomeStatementPeriodEndDate" contextRef="Duration_2024" format="date">December 31, 2024</ix:nonFraction></p>

    <table>
        <tr>
            <td>Revenues</td>
            <td>$<ix:nonFraction name="us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax" contextRef="Duration_2024" unitRef="USD" decimals="-3">12500000</ix:nonFraction></td>
        </tr>
        <tr>
            <td>Cost of Revenues</td>
            <td>$<ix:nonFraction name="us-gaap:CostOfRevenue" contextRef="Duration_2024" unitRef="USD" decimals="-3">7200000</ix:nonFraction></td>
        </tr>
        <tr>
            <td><strong>Gross Profit</strong></td>
            <td><strong>$<ix:nonFraction name="us-gaap:GrossProfit" contextRef="Duration_2024" unitRef="USD" decimals="-3">5300000</ix:nonFraction></strong></td>
        </tr>
        <tr>
            <td>Operating Expenses</td>
            <td>$<ix:nonFraction name="us-gaap:OperatingExpenses" contextRef="Duration_2024" unitRef="USD" decimals="-3">3800000</ix:nonFraction></td>
        </tr>
        <tr>
            <td><strong>Net Income</strong></td>
            <td><strong>$<ix:nonFraction name="us-gaap:NetIncomeLoss" contextRef="Duration_2024" unitRef="USD" decimals="-3">1500000</ix:nonFraction></strong></td>
        </tr>
    </table>
</body>
</html>"""

    with open("sample_ixbrl_financials.html", 'w', encoding='utf-8') as f:
        f.write(ixbrl_content)

    print("✓ Created sample Inline XBRL file: sample_ixbrl_financials.html\n")
    return ixbrl_content

def parse_ixbrl_with_claude(ixbrl_file: str = "sample_ixbrl_financials.html"):
    """Use Claude with code execution to parse XBRL and extract facts"""

    # Read the XBRL file
    try:
        with open(ixbrl_file, 'r', encoding='utf-8') as f:
            ixbrl_content = f.read()
    except FileNotFoundError:
        print(f"Creating sample XBRL file...\n")
        ixbrl_content = create_sample_ixbrl()

    print("Parsing Inline XBRL with Claude...\n")

    client = anthropic.Anthropic()

    response = client.beta.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=4096,
        betas=["code-execution-2025-08-25"],
        tools=[
            {
                "type": "code_execution_20250825",
                "name": "code_execution"
            }
        ],
        messages=[
            {
                "role": "user",
                "content": f"""Parse this Inline XBRL financial statement and extract all XBRL facts.

XBRL Content:
{ixbrl_content}

Using code execution, please:
1. Parse the HTML and extract all XBRL facts (ix:nonFraction elements)
2. For each fact, extract:
   - Element name (from 'name' attribute)
   - Value (the text content)
   - Context (from 'contextRef')
   - Unit (from 'unitRef')
   - Decimals (from 'decimals')
3. Organize the facts into a structured JSON format
4. Perform basic validation:
   - Check if Assets = Liabilities + Equity
   - Check if Gross Profit = Revenue - Cost of Revenue
   - Calculate key ratios (current ratio, debt to equity)

Return the parsed data as JSON with this structure:
{{
  "facts": [
    {{
      "element": "us-gaap:Assets",
      "value": 13132000,
      "context": "AsOf_2024-12-31",
      "unit": "USD",
      "decimals": "-3",
      "label": "Total Assets"
    }}
  ],
  "validation": {{
    "balance_sheet_balances": true/false,
    "income_statement_math": true/false,
    "errors": []
  }},
  "ratios": {{
    "current_ratio": 3.14,
    "debt_to_equity": 0.43,
    "gross_margin_pct": 42.4,
    "net_margin_pct": 12.0
  }}
}}

Use BeautifulSoup or similar library for parsing."""
            }
        ]
    )

    # Extract the response
    print("XBRL Parsing Results:\n")
    print("="*60)

    for block in response.content:
        if block.type == 'text':
            print(block.text)
            print("="*60)

    return response

def generate_xbrl_audit_report():
    """Generate an Excel audit workpaper from parsed XBRL data"""

    print("\nGenerating audit workpaper from XBRL data...\n")

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
        messages=[
            {
                "role": "user",
                "content": """First, parse the XBRL file 'sample_ixbrl_financials.html', then create an Excel audit workpaper with:

Sheet 1 - "XBRL Facts Extract":
- All extracted XBRL facts in a table
- Columns: Element Name, Value, Context, Unit, Label
- Group by statement (Balance Sheet vs Income Statement)

Sheet 2 - "Mathematical Validation":
- Balance Sheet equation check (Assets = Liabilities + Equity)
- Income Statement calculations
- Show expected vs actual values
- Highlight any discrepancies

Sheet 3 - "Financial Ratios":
- Current Ratio
- Debt to Equity
- Gross Margin %
- Net Margin %
- Include benchmarks and commentary

Sheet 4 - "Audit Procedures":
- List suggested audit procedures for each major XBRL element
- Link to specific accounts (e.g., "Cash" -> "Perform bank reconciliation")
- Risk assessment for each element

Use professional formatting with color coding for any validation errors."""
            }
        ]
    )

    # Extract file
    file_id = None
    for block in response.content:
        if hasattr(block, 'file_id') and block.file_id:
            file_id = block.file_id
            break

    if file_id:
        file_content = client.beta.files.retrieve_content(file_id)
        output_filename = "xbrl_audit_analysis.xlsx"

        with open(output_filename, 'wb') as f:
            f.write(file_content)

        print(f"✓ XBRL audit analysis saved to: {output_filename}")
        print(f"  File size: {len(file_content) / 1024:.1f} KB\n")
        return output_filename
    else:
        print("✗ No file generated\n")
        return None

if __name__ == "__main__":
    # Create sample XBRL if needed
    import os
    if not os.path.exists("sample_ixbrl_financials.html"):
        create_sample_ixbrl()

    # Parse XBRL with Claude
    print("STEP 1: Parse XBRL document\n")
    parse_ixbrl_with_claude()

    print("\n" + "="*60)
    print("\nSTEP 2: Generate Excel audit workpaper from XBRL data\n")
    generate_xbrl_audit_report()

    print("\nNext steps:")
    print("1. Review the generated Excel workpaper")
    print("2. Compare XBRL facts with audit checklist procedures")
    print("3. Proceed to cross-referencing (Phase 4)")
