from agents.pre_writing import JobAnalyzer, ClientAnalyzer
from agents.writing_suite import Strategist, HookGenerator, Writer, QASolver, Critic
from database.vector_store import RankingEngine
from utils.knowledge_vault import KnowledgeVault
from utils.feedback_loop import FeedbackLoop

class EliteProposalWorkflow:
    def __init__(self):
        self.job_analyzer = JobAnalyzer()
        self.client_analyzer = ClientAnalyzer()
        self.strategist = Strategist()
        self.hook_generator = HookGenerator()
        self.writer = Writer()
        self.qa_solver = QASolver()
        self.critic = Critic()
        self.ranking_engine = RankingEngine()
        self.knowledge_vault = KnowledgeVault()
        self.feedback_loop = FeedbackLoop()

    def run(self, job_description, client_history="", screening_questions=None):
        print("--- Starting Elite Proposal Workflow ---")
        
        # 1. Intelligence Phase
        print("[1/6] Analyzing Job & Client...")
        job_analysis = self.job_analyzer.analyze(job_description)
        client_analysis = self.client_analyzer.analyze(client_history)
        
        # 2. Strategy Phase
        print("[2/6] Developing Strategy...")
        strategy = self.strategist.create_strategy(job_analysis, client_analysis)
        
        # 3. Knowledge Retrieval
        print("[3/6] Retrieving Relevant Portfolio & Knowledge...")
        relevant_projects = self.ranking_engine.search_and_rank(
            job_description, 
            required_tech=job_analysis.get('tech_stack', [])
        )
        
        # New V2: Knowledge Vault Retrieval
        knowledge_items = self.knowledge_vault.get_all_knowledge()
        # Filter knowledge items that match tech stack (simple keyword match for now)
        relevant_knowledge = []
        for item in knowledge_items:
            for tech in job_analysis.get('tech_stack', []):
                if tech.lower() in item['snippet'].lower():
                    relevant_knowledge.append(item)
                    break
        
        # New V2: Feedback Loop (Few-shot learning)
        winning_examples = self.feedback_loop.get_winning_examples(limit=2)
        
        # 4. Writing Phase
        print("[4/6] Generating Hooks & Draft...")
        hooks = self.hook_generator.generate_hooks(strategy, job_analysis.get('intent', ''))
        
        state = {
            "job_analysis": job_analysis,
            "client_analysis": client_analysis,
            "strategy": strategy,
            "hooks": hooks,
            "relevant_projects": relevant_projects,
            "relevant_knowledge": relevant_knowledge,
            "winning_examples": winning_examples,
            "job_description": job_description
        }
        
        proposal = self.writer.write_draft(state)
        
        # 5. Question Solving
        if screening_questions:
            print("[5/6] Solving Screening Questions...")
            qa_answers = self.qa_solver.solve_questions(screening_questions, job_analysis.get('tech_stack', []))
            proposal['qa_answers'] = qa_answers

        # 6. Quality Wall (Critic Loop)
        print("[6/6] Entering Quality Wall...")
        max_retries = 2
        for i in range(max_retries):
            review = self.critic.review(proposal['draft'], job_description)
            print(f"   Critic Score: {review.get('score', 'N/A')}/10")
            
            if review.get('action') == 'pass' or i == max_retries - 1:
                break
            
            print(f"   Redrafting based on feedback: {review.get('feedback', [])}")
            state['critic_feedback'] = review.get('feedback', [])
            proposal = self.writer.write_draft(state)

        print("--- Workflow Complete ---")
        return {
            "proposal": proposal,
            "analysis": {
                "job": job_analysis,
                "client": client_analysis
            },
            "strategy": strategy,
            "score": review.get('score', 0)
        }

if __name__ == "__main__":
    workflow = EliteProposalWorkflow()
    # Mock data for testing
    job_desc = "Looking for a Shopify expert to automate my inventory via Python."
    result = workflow.run(job_desc)
    print(json.dumps(result, indent=2))
