from fastapi import FastAPI, File, UploadFile, Form, HTTPException, BackgroundTasks
import os
import uuid
import sqlite3

from crewai import Crew, Process
from agents import financial_analyst
from task import financial_analysis_task

app = FastAPI(title="Financial Document Analyzer")

DATABASE = "analysis.db"


# ---------- DATABASE SETUP ----------
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis_results (
            id TEXT PRIMARY KEY,
            query TEXT,
            result TEXT
        )
    """)

    conn.commit()
    conn.close()

init_db()


# ---------- CREW RUNNER ----------
def run_crew(query: str):

    try:
        financial_crew = Crew(
            agents=[financial_analyst],
            tasks=[financial_analysis_task],
            process=Process.sequential,
        )

        result = financial_crew.kickoff(inputs={"query": query})
        return str(result)

    except Exception as e:

        print("LLM execution failed. Using fallback mock response.")
        print("Error:", e)

        # SAFE FALLBACK (only if API fails)
        mock_result = f"""
Mock Analysis (Fallback Mode)

The system could not access external LLM services.
Returning fallback analysis to maintain pipeline stability.

Query received:
{query}

Sample Investment Insight:
- Market volatility appears elevated.
- Diversification recommended.
- Further analysis required with full LLM access.
"""

        return mock_result


# ---------- BACKGROUND WORKER ----------
def process_analysis(job_id: str, query: str):

    result = run_crew(query)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO analysis_results VALUES (?, ?, ?)",
        (job_id, query, result),
    )

    conn.commit()
    conn.close()


@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}


@app.post("/analyze")
async def analyze(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document"),
):

    job_id = str(uuid.uuid4())

    os.makedirs("data", exist_ok=True)
    file_path = f"data/{job_id}.pdf"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    background_tasks.add_task(process_analysis, job_id, query)

    return {
        "status": "queued",
        "job_id": job_id,
        "message": "Analysis started in background worker"
    }


@app.get("/result/{job_id}")
async def get_result(job_id: str):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT result FROM analysis_results WHERE id=?",
        (job_id,),
    )

    data = cursor.fetchone()
    conn.close()

    if not data:
        return {"status": "processing"}

    return {"status": "completed", "analysis": data[0]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)