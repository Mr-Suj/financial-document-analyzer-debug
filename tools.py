from crewai.tools import BaseTool
from crewai_tools import SerperDevTool, PDFSearchTool

search_tool = SerperDevTool()

class FinancialDocumentTool(BaseTool):
    name: str = "Financial Document Reader"
    description: str = "Reads financial PDF documents and returns cleaned text."

    def _run(self, path: str = 'data/sample.pdf') -> str:
        pdf_tool = PDFSearchTool()
        docs = pdf_tool.run(path)
        return docs


class InvestmentTool(BaseTool):
    name: str = "Investment Analysis Tool"
    description: str = "Analyzes investment insights from financial data."

    def _run(self, financial_document_data: str) -> str:
        return "Investment analysis functionality to be implemented"


class RiskTool(BaseTool):
    name: str = "Risk Assessment Tool"
    description: str = "Creates risk assessment from financial data."

    def _run(self, financial_document_data: str) -> str:
        return "Risk assessment functionality to be implemented"