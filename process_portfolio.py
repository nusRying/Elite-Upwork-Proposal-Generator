import os
import re

SOURCE_DIR = "all_readmes"
TARGET_DIR = "portfolio"

# Comprehensive list of technologies for better extraction
TECH_KEYWORDS = [
    "SolidWorks", "Python", "Shopify", "React", "AI", "nTopology", 
    "LangGraph", "Ollama", "FastAPI", "TensorFlow", "PyTorch", 
    "TypeScript", "Next.js", "C++", "C#", "Dart", "Flutter", 
    "Keras", "OpenCV", "Scikit-Learn", "Firebase", "PostgreSQL",
    "Arduino", "ESP32", "MATLAB", "CircuitVerse", "Node.js", 
    "Tailwind CSS", "MongoDB", "Docker", "Kubernetes", "AWS", "Azure"
]

def clean_text(text):
    # Remove markdown links, markers, and excess whitespace
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    text = re.sub(r'[#*`≡Γ]', '', text)
    return ' '.join(text.split())

def extract_skills(content):
    skills = []
    for tech in TECH_KEYWORDS:
        if tech.lower() in content.lower():
            skills.append(tech)
    return skills

def process_readmes():
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith(".md")]
    print(f"Found {len(files)} READMEs to process.")

    for filename in files:
        source_path = os.path.join(SOURCE_DIR, filename)
        repo_name = filename.replace(".README.md", "")
        target_path = os.path.join(TARGET_DIR, f"{repo_name}.txt")
        repo_link = f"https://github.com/nusRying/{repo_name}"

        with open(source_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        content = "".join(lines)
        
        # Extract title
        title = repo_name
        for line in lines:
            if line.startswith("#"):
                title = line.strip("# \n")
                break
        
        # Extract skills/tech
        skills = extract_skills(content)
        tech_stack = ", ".join(skills) if skills else "General Engineering"
        
        # Extract a summary
        summary_parts = []
        for line in lines[2:]: # Skip title
            if line.startswith("#") or "Tech Stack" in line or "Features" in line:
                break
            if line.strip():
                summary_parts.append(line.strip())
            if len(summary_parts) > 2:
                break
        
        summary = " ".join(summary_parts)
        if not summary:
            summary = f"A GitHub repository for {title}."

        # Write enriched structured output
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(f"Project: {title}\n")
            f.write(f"Link: {repo_link}\n")
            f.write(f"Tech: {tech_stack}\n")
            f.write(f"Skills: {', '.join(skills)}\n")
            f.write(f"Outcome: {clean_text(summary)}\n")
            f.write(f"Source: GitHub Repository ({repo_name})\n")
            f.write("Year: 2024\n")
            f.write("Status: Completed\n")

    print(f"Enriched and processed {len(files)} projects into {TARGET_DIR}.")

if __name__ == "__main__":
    process_readmes()
