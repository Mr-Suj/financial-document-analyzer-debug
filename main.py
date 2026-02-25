from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid

# NOTE:
# We keep imports minimal because we are running in MOCK MODE
# to avoid OpenAI quota issues.

app = FastAPI(title="Financial Document Analyzer")


# ============================================
# MOCK CREW EXECUTION (No OpenAI Required)
# ============================================

def run_crew(query: str, file_path: str = "data/sample.pdf"):
    """
    Mocked Crew execution.
    This simulates AI output without calling any external API.
    """

    mock_response = f"""
    Financial Analysis Report (Mocked Response)

    Query:
    {query}

    ---------------------------------------
    Summary:
    - Revenue trend appears stable with moderate YoY growth.
    - Operating margins show slight compression.
    - Cash flow remains positive.

    Investment Insights:
    - Consider long-term holding strategy.
    - Diversification recommended.
    - Monitor macroeconomic indicators.

    Risk Factors:
    - Market volatility
    - Regulatory changes
    - Sector competition

    NOTE:
    This is a mocked AI response used for debugging demonstration.
    """

    return mock_response


# ============================================
# API ENDPOINTS
# ============================================

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Financial Document Analyzer API is running"}


@app.post("/analyze")
async def analyze_financial_document(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):
    """
    Analyze financial document and provide investment recommendations
    """

    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"

    try:
        # Ensure data folder exists
        os.makedirs("data", exist_ok=True)

        # Save uploaded file
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Validate query
        if not query:
            query = "Analyze this financial document for investment insights"

        # Run mocked AI analysis
        response = run_crew(query=query.strip(), file_path=file_path)

        return {
            "status": "success",
            "query": query,
            "analysis": response,
            "file_processed": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing financial document: {str(e)}")

    finally:
        # Cleanup uploaded file
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass


# ============================================
# RUN SERVER
# ============================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)