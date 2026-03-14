from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from workflow import EliteProposalWorkflow
from utils.knowledge_vault import KnowledgeVault
from utils.feedback_loop import FeedbackLoop
import os
import shutil

app = FastAPI(title="Elite Upwork Proposal Assistant")

# Enable CORS for the React dashboard
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

workflow = EliteProposalWorkflow()
knowledge_vault = KnowledgeVault()
feedback_loop = FeedbackLoop()

class ProposalRequest(BaseModel):
    job_description: str
    job_type: str = "project"  # Default to project
    client_history: Optional[str] = ""
    screening_questions: Optional[List[str]] = []

class StatusUpdateRequest(BaseModel):
    proposal_id: int
    status: str
    notes: Optional[str] = ""

@app.post("/generate")
async def generate_proposal(request: ProposalRequest):
    try:
        result = workflow.run(
            request.job_description,
            request.job_type,
            request.client_history,
            request.screening_questions
        )
        # Save to Feedback Loop
        proposal_id = feedback_loop.save_proposal(
            request.job_description, 
            result['proposal']['draft']
        )
        result['proposal_id'] = proposal_id
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/knowledge/upload")
async def upload_knowledge(file: UploadFile = File(...)):
    temp_path = f"data/knowledge/{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        filename = knowledge_vault.ingest_file(temp_path)
        return {"status": "success", "filename": filename}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/knowledge")
async def list_knowledge():
    return {"items": knowledge_vault.get_all_knowledge()}

@app.delete("/knowledge/{item_id}")
async def delete_knowledge(item_id: int):
    knowledge_vault.delete_knowledge(item_id)
    return {"status": "success"}

@app.post("/proposals/status")
async def update_proposal_status(request: StatusUpdateRequest):
    feedback_loop.update_status(request.proposal_id, request.status, request.notes)
    return {"status": "success", "message": f"Proposal {request.proposal_id} marked as {request.status}"}

@app.post("/external/scrape")
async def handle_scrape(data: dict):
    # Endpoint for browser extension
    return {"status": "received", "data": data}

@app.get("/portfolio")
async def get_portfolio():
    # Keep legacy portfolio for now
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
