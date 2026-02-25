# Financial Document Analyzer – Debug Challenge Submission

## Overview

This project is a fixed and enhanced version of a buggy CrewAI-based financial document analysis system.

The original system contained multiple architectural and dependency issues that prevented it from running correctly.  
This submission includes:

- Full debugging and stabilization
- Production-style architecture improvements
- Background job processing
- Database integration
- Environment-based API configuration

The system now runs end-to-end using CrewAI agents to analyze uploaded financial documents.

---

## Original Issues Identified & Fixed

During debugging, the following major issues were identified:

### 1. Dependency Conflicts
- CrewAI version mismatch with `pydantic`
- Conflicting `opentelemetry` versions
- OpenAI SDK version incompatibilities

**Fix:** Cleaned `requirements.txt` and aligned compatible versions.

---

### 2. Incorrect CrewAI Usage
- Improper Agent imports
- Tools not inheriting from `BaseTool`
- Pydantic validation failures
- Invalid task-tool configuration

**Fix:**  
- Updated to latest CrewAI API usage  
- Converted tools to proper `BaseTool` implementations  
- Fixed task and agent initialization logic  

---

### 3. FastAPI Runtime Errors
- Missing `python-multipart`
- Blocking request handling
- No concurrency model

**Fix:**  
- Installed required dependencies  
- Implemented Background Task processing  

---

### 4. OpenAI Quota Failure Handling 
During testing, API quota errors occurred (I don't have paid API key).

**Engineering Decision:**
- Implemented graceful fallback mode
- Preserved pipeline integrity
- Prevented system crashes

The system now:
- Uses real LLM if API key is valid
- Falls back to mock analysis only if LLM fails

---

## Architecture Overview

### 1. FastAPI Backend
- REST API endpoints
- Swagger documentation (`/docs`)
- Non-blocking request handling

### 2. CrewAI Multi-Agent System
- Financial Analyst agent
- Structured financial analysis task
- Tool-based PDF reader

### 3. Background Worker Model (Bonus)
Implemented using `FastAPI BackgroundTasks`.

Flow:
1. User uploads financial document
2. Job is queued
3. Background worker processes analysis
4. Result stored in database
5. User retrieves result via job_id

This simulates a lightweight queue-worker architecture.

---

### 4. Database Integration (Bonus)
- SQLite used for persistence
- Stores:
  - job_id
  - user query
  - generated analysis
- Endpoint provided to fetch results

Table Schema:

```
analysis_results (
    id TEXT PRIMARY KEY,
    query TEXT,
    result TEXT
)
```

---

## Project Structure

```
financial-document-analyzer-debug/
│
├── main.py              # FastAPI server + background worker
├── agents.py            # CrewAI agent definitions
├── task.py              # Structured analysis task
├── tools.py             # Custom BaseTool implementations
├── requirements.txt
├── .env.example         # Environment variable template
├── .gitignore
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/Mr-Suj/financial-document-analyzer-debug.git
cd financial-document-analyzer-debug
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Copy the example file:

```bash
copy .env.example .env
```

Then edit `.env` and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

---

## Running the Server

```bash
python main.py
```

Open:

```
http://localhost:8000/docs
```

---

## API Endpoints

### POST `/analyze`

Uploads a financial document and starts background analysis.

Returns:

```json
{
  "status": "queued",
  "job_id": "uuid"
}
```

---

### GET `/result/{job_id}`

Retrieves analysis result.

Possible responses:

```json
{
  "status": "processing"
}
```

or

```json
{
  "status": "completed",
  "analysis": "Generated financial analysis..."
}
```

---

## Fallback Mode

If:
- API key is invalid
- OpenAI quota is exceeded
- External API fails

The system returns a structured mock response instead of crashing.

This ensures:
- Pipeline stability
- Testability without external dependency
- Clean debugging workflow

---

## Key Engineering Improvements

- Cleaned and stabilized dependency tree
- Migrated to correct CrewAI API usage
- Implemented production-style environment config
- Added background job processing
- Added database persistence layer
- Implemented graceful LLM failure handling
- Structured financial analysis task

---

## Final Notes

This submission focuses on:

- Correct debugging methodology
- Production-safe API integration
- Scalable backend structure
- Clean separation of concerns
- Resilient system design

The system is fully functional and extensible for real-world financial analysis workflows.
---

## 👨‍💻 Author

Sujal Gowda  J M
