from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from workflow import EliteProposalWorkflow
import os

app = FastAPI(title="Elite Upwork Proposal Assistant")

# Enable CORS for the React dashboard
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

workflow = EliteProposalWorkflow()

class ProposalRequest(BaseModel):
    job_description: str
    client_history: Optional[str] = ""
    screening_questions: Optional[List[str]] = []

@app.post("/generate")
async def generate_proposal(request: ProposalRequest):
    try:
        result = workflow.run(
            request.job_description,
            request.client_history,
            request.screening_questions
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/portfolio")
async def get_portfolio():
    portfolio_dir = "portfolio"
    if not os.path.exists(portfolio_dir):
        return {"projects": []}
    
    projects = []
    for filename in os.listdir(portfolio_dir):
        if filename.endswith(('.txt', '.pdf')):
            projects.append(filename)
    return {"projects": projects}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
