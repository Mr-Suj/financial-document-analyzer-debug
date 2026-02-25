# Financial Document Analyzer – CrewAI Debug Challenge Submission

## Overview

This repository contains a fully debugged and production-stabilized version of the original buggy CrewAI-based Financial Document Analyzer system provided in the assignment.

The original codebase contained dependency conflicts, incorrect CrewAI usage, unsafe agent prompt design, and runtime instability.

This submission includes:

- Full debugging and dependency resolution
- Correct CrewAI agent-task orchestration
- Production-style environment configuration
- Background job processing (queue-like model)
- SQLite database integration
- Graceful LLM failure handling with fallback mode
- Responsible agent prompt redesign

The system now runs end-to-end as a stable REST API using FastAPI + CrewAI.

---

## Bugs Identified & Fixes Implemented

### 1. Dependency Conflicts & Version Mismatch

Issues:
- CrewAI incompatible with pinned `pydantic` version
- Conflicting `opentelemetry` dependencies
- OpenAI SDK version mismatch
- Improper package resolution

Fix:
- Rebuilt and cleaned `requirements.txt`
- Aligned versions with CrewAI documentation
- Recreated virtual environment
- Verified compatibility with Python 3.11

---

### 2. Incorrect CrewAI Integration

Issues:
- Improper `Agent` imports
- Tools not inheriting from `BaseTool`
- Pydantic validation failures
- Incorrect task-tool wiring
- Invalid `kickoff()` usage

Fix:
- Updated to correct CrewAI quickstart pattern
- Converted tools to proper `BaseTool` classes
- Corrected `Task` configuration
- Ensured proper `Crew(...).kickoff(inputs={})` usage
- Validated sequential process execution

---

### 3. Unsafe Agent Prompt Design (Critical Fix)

The original agents contained instructions that:

- Encouraged hallucinated financial advice
- Ignored regulatory considerations
- Promoted fabricated investment recommendations
- Approved documents without validation

Engineering Decision:

Redesigned agent backstories to:

- Enforce responsible financial reasoning
- Avoid hallucinated claims
- Focus on data-driven analysis
- Align with production-grade LLM usage

This significantly improves system reliability and AI safety.

---

### 4. FastAPI Runtime & Concurrency Issues

Issues:
- Missing `python-multipart`
- Blocking request execution
- No job tracking mechanism

Fix:
- Installed required runtime dependencies
- Implemented `BackgroundTasks`
- Added job_id-based asynchronous processing

---

### 5. OpenAI Quota / External API Failure

During testing, quota limits were encountered.

Engineering Decision:

Implemented graceful fallback mode:

- System attempts real LLM call
- If LLM fails (quota, invalid key, network), fallback response is returned
- API never crashes
- Pipeline remains testable without paid key

This ensures architectural robustness independent of external API stability.

---

## Architecture Overview

### 1. FastAPI REST Layer

- Swagger UI available at `/docs`
- Non-blocking job submission
- Background execution
- Result polling endpoint

Endpoints:

- POST `/analyze`
- GET `/result/{job_id}`

---

### 2. CrewAI Multi-Agent Orchestration

Follows official CrewAI quickstart pattern:

- Agent definition
- Task definition
- Crew orchestration
- Sequential execution
- kickoff(inputs={})

System Components:

- Financial Analyst Agent
- Structured Financial Analysis Task
- PDF Tool (BaseTool implementation)

---

### 3. Background Worker Model (Bonus Requirement)

Implemented using FastAPI `BackgroundTasks`.

Flow:

1. User uploads financial document
2. Server generates job_id
3. Background worker executes Crew
4. Result stored in database
5. User polls result using job_id

This simulates a lightweight queue-based architecture.

---

### 4. Database Integration (Bonus Requirement)

SQLite database used for persistence.

Stores:

- job_id
- user query
- analysis result

Table Schema:

analysis_results (
    id TEXT PRIMARY KEY,
    query TEXT,
    result TEXT
)

Provides state tracking and supports concurrent requests.

---

## Project Structure

financial-document-analyzer-debug/
│
├── main.py              # FastAPI server + background worker + DB
├── agents.py            # CrewAI agent definitions
├── task.py              # Financial analysis task configuration
├── tools.py             # Custom BaseTool implementations
├── requirements.txt
├── .env.example         # Environment variable template
├── .gitignore
└── README.md

---

## Setup Instructions

### 1. Clone Repository

git clone https://github.com/Mr-Suj/financial-document-analyzer-debug.git
cd financial-document-analyzer-debug

### 2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Configure Environment Variables

Copy template:

copy .env.example .env

Edit `.env`:

OPENAI_API_KEY=your_api_key_here

Recruiter can use company-provided API key for testing.

---

## Running the Application

python main.py

Open Swagger UI:

http://localhost:8000/docs

---

## API Documentation

### POST `/analyze`

Uploads financial document and starts background analysis.

Response:

{
  "status": "queued",
  "job_id": "uuid"
}

### GET `/result/{job_id}`

Processing:

{
  "status": "processing"
}

Completed:

{
  "status": "completed",
  "analysis": "Generated financial analysis..."
}

---

## Fallback Mode

If:

- API key invalid
- Quota exceeded
- LLM call fails

System returns structured fallback response.

Benefits:

- No crashes
- Stable API behavior
- Testable without paid key
- Clean debugging workflow

---

## Key Engineering Improvements

- Resolved complex dependency conflicts
- Migrated to correct CrewAI architecture
- Fixed tool validation issues
- Implemented environment-based API configuration
- Added queue-style background processing
- Integrated database persistence
- Implemented resilient LLM fallback handling
- Redesigned unsafe prompt logic
- Ensured clean Git hygiene (.env, venv, database ignored)

---

## Alignment With CrewAI Documentation

System follows official CrewAI quickstart pattern:

- Agent
- Task
- Crew
- kickoff()
- Tool-based execution

Extended with production-grade API layer and persistence.

---

## Conclusion

This submission demonstrates:

- Systematic debugging methodology
- Production-aware AI integration
- Clean backend architecture
- Responsible prompt engineering
- Resilient API design
- Bonus feature implementation

The application is fully functional, extensible, and stable under both real LLM and fallback modes.

---

## Author

Sujal Gowda J M