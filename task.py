## Importing libraries and files
from crewai import Task
from agents import financial_analyst
from tools import FinancialDocumentTool


# ===============================
# Primary Financial Analysis Task
# ===============================

financial_analysis_task = Task(
    description="""
Analyze the provided financial document in relation to the user query: {query}

Your responsibilities:
- Extract key financial metrics and performance indicators
- Identify revenue trends, profitability signals, and cost structures
- Highlight potential financial risks
- Provide structured investment insights
- Base conclusions on the document content rather than assumptions

Maintain clarity, logical reasoning, and financial accuracy.
""",

    expected_output="""
Provide a structured financial analysis including:

1. Executive Summary
2. Key Financial Observations
3. Risk Assessment
4. Investment Considerations
5. Final Recommendation

Use clear headings and bullet points where appropriate.
Avoid speculation beyond available financial data.
""",

    agent=financial_analyst,
    tools=[FinancialDocumentTool()],
    async_execution=False,
)