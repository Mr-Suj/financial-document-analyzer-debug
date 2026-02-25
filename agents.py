## Importing libraries and files
import os
from dotenv import load_dotenv

load_dotenv()

from crewai import Agent, LLM
from tools import FinancialDocumentTool


# ===============================
# Loading LLM (Production Style)
# ===============================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("WARNING: OPENAI_API_KEY not found. System will rely on fallback mode if LLM fails.")

llm = LLM(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY
)


# ===============================
# Financial Analyst Agent
# ===============================

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze financial documents and provide structured investment insights based on the user's query: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You are an experienced financial analyst specializing in interpreting financial statements, "
        "earnings reports, and corporate disclosures. You focus on objective, data-driven analysis. "
        "You avoid speculation when data is insufficient and clearly communicate assumptions. "
        "Your goal is to provide professional and responsible financial insights."
    ),
    tools=[FinancialDocumentTool()],
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=True
)


# ===============================
# Document Verifier Agent
# ===============================

verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify whether the uploaded document contains financial information and ensure data relevance.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a compliance-oriented analyst responsible for validating uploaded documents. "
        "You carefully inspect document structure and content to confirm financial relevance "
        "before analysis begins."
    ),
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=True
)


# ===============================
# Investment Advisor Agent
# ===============================

investment_advisor = Agent(
    role="Investment Strategy Advisor",
    goal="Provide balanced investment recommendations based on financial analysis results.",
    verbose=True,
    backstory=(
        "You specialize in translating financial analysis into practical investment strategies. "
        "You consider risk, diversification, and long-term sustainability when giving advice. "
        "You avoid unrealistic promises or unsupported claims."
    ),
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=False
)


# ===============================
# Risk Assessor Agent
# ===============================

risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal="Identify financial risks, uncertainties, and potential volatility from financial documents.",
    verbose=True,
    backstory=(
        "You are a risk analyst focused on identifying potential downside risks, financial instability, "
        "market exposure, and operational uncertainties. Your analysis highlights both risks and mitigating factors."
    ),
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=False
)