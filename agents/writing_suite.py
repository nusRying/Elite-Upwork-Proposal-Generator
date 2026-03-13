from agents.pre_writing import BaseAgent
import json

class Strategist(BaseAgent):
    def __init__(self):
        super().__init__("llama3.2:3b") # Reasoning on 3B-instruct fits perfectly in VRAM

    def create_strategy(self, job_analysis, client_analysis):
        prompt = f"""
        Job Analysis: {job_analysis}
        Client Analysis: {client_analysis}

        Based on the above, create a proposal strategy in JSON format:
        {{
            "hook_style": "Pain-Point / Insight / Result-First",
            "priority_projects": ["Titles and why these are relevant"],
            "tone": "Casual/Formal/Technical/Consultative",
            "pricing_approach": "How to frame the price (e.g., 'Value-based' or 'Milestone-focused')",
            "unique_selling_point": "The one thing that will win this job"
        }}
        """
        return self.query(prompt)

class HookGenerator(BaseAgent):
    def __init__(self):
        super().__init__("llama3.2:3b") # Creative and fast

    def generate_hooks(self, strategy, job_intent):
        prompt = f"""
        Strategy: {strategy}
        Job Intent: {job_intent}

        Generate 3 high-impact hooks (first 2 lines of the proposal) following the strategy:
        {{
            "hooks": [
                "Hook 1: Pain Centric",
                "Hook 2: Insight Driven",
                "Hook 3: Direct Result"
            ]
        }}
        """
        return self.query(prompt)

class Writer(BaseAgent):
    def __init__(self):
        super().__init__("llama3.2:3b")

    def write_draft(self, state):
        prompt = f"""
        State: {json.dumps(state)}
        System Knowledge (Relevant Projects): {state.get('relevant_projects', [])}

        Write a full Upwork proposal based on the strategy and hook provided.
        Format in JSON:
        {{
            "draft": "Full proposal text",
            "word_count": 0
        }}
        """
        return self.query(prompt)

class QASolver(BaseAgent):
    def __init__(self):
        super().__init__("phi3:mini")

    def solve_questions(self, questions, tech_stack):
        prompt = f"""
        Questions: {questions}
        Tech Stack: {tech_stack}
        
        Answer the screening questions with 'Proof + Clarification' logic.
        JSON format:
        {{
            "answers": [{{ "question": "...", "answer": "..." }}]
        }}
        """
        return self.query(prompt)

class Critic(BaseAgent):
    def __init__(self):
        super().__init__("phi3:mini") # Fast evaluation

    def review(self, draft, job_description):
        prompt = f"""
        Draft: {draft}
        Job: {job_description}

        Review the proposal for Relevance, Persuasion, and Clarity.
        JSON format:
        {{
            "score": 0-10,
            "feedback": ["List of improvements"],
            "generic_boilerplate_detected": true/false,
            "action": "pass/rewrite"
        }}
        """
        return self.query(prompt)

if __name__ == "__main__":
    strategist = Strategist()
    print("Strategist Initialized.")
