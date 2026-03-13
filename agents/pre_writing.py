import requests
import json

class BaseAgent:
    def __init__(self, model):
        self.model = model
        self.endpoint = "http://localhost:11434/api/generate"

    def query(self, prompt, system_prompt=""):
        try:
            response = requests.post(
                self.endpoint,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "system": system_prompt,
                    "stream": False,
                    "format": "json"
                },
                timeout=120
            )
            response.raise_for_status()
            res_json = response.json()
            if "response" in res_json:
                try:
                    return json.loads(res_json["response"])
                except:
                    return res_json["response"]
            return {"error": "No response field in Ollama output"}
        except Exception as e:
            print(f"Agent Error ({self.model}): {str(e)}")
            return {"error": str(e)}

class JobAnalyzer(BaseAgent):
    def __init__(self):
        super().__init__("phi3:mini") # Extraction is best on small efficient models

    def analyze(self, job_description):
        system_prompt = """
        You are an Elite Upwork Job Analyst. 
        Analyze the job description and extract the following in JSON format:
        {
            "intent": "What is the client actually trying to achieve?",
            "deliverables": ["List of core items"],
            "tech_stack": ["Required technologies"],
            "difficulty": "Easy/Medium/Hard",
            "hidden_needs": "What they didn't say but probably need",
            "questions_to_ask": ["High-value clarifying questions"]
        }
        """
        return self.query(job_description, system_prompt)

class ClientAnalyzer(BaseAgent):
    def __init__(self):
        super().__init__("phi3:mini")

    def analyze(self, client_history):
        system_prompt = """
        Analyze the client's past hiring history and reviews to extract:
        {
            "avg_rating": "Numeric",
            "communication_style": "Brief/Detailed/Technical",
            "pain_points": ["What they complained about in past reviews"],
            "ideal_candidate_traits": ["Skills they frequently hire for"],
            "client_name": "Extract if mentioned in reviews (frequently 'Thanks, [Name]')",
            "estimated_budget_tier": "Low/Mid/High"
        }
        """
        return self.query(client_history, system_prompt)

if __name__ == "__main__":
    analyzer = JobAnalyzer()
    print("Job Analyzer Initialized.")
