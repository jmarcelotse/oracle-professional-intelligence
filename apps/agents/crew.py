"""Agentes CrewAI do Oracle.

Exemplo inicial: três agentes (LinkedIn Writer, Resume Optimizer, Career
Strategist) e uma task de criação de post. Os agentes usam o gateway LiteLLM
apontando para modelos locais do Ollama (ver LITELLM_BASE_URL no .env).
"""
import os

from crewai import Agent, Task, Crew

# LiteLLM expõe API compatível com OpenAI; CrewAI/litellm consomem via env.
os.environ.setdefault(
    "OPENAI_API_BASE",
    os.getenv("LITELLM_BASE_URL", "http://localhost:4000"),
)
os.environ.setdefault("OPENAI_API_KEY", "sk-local")

linkedin_writer = Agent(
    role="LinkedIn Writer",
    goal="Criar conteúdo técnico para fortalecer autoridade profissional.",
    backstory="Especialista em DevOps, SRE, AWS, Kubernetes, Terraform, DevSecOps e FinOps.",
)

resume_optimizer = Agent(
    role="Resume Optimizer",
    goal="Adaptar currículos para vagas internacionais de tecnologia.",
    backstory="Especialista em ATS, recrutamento internacional e currículos técnicos.",
)

career_strategist = Agent(
    role="Career Strategist",
    goal="Criar planos de carreira e posicionamento profissional.",
    backstory="Especialista em carreira internacional para profissionais de tecnologia.",
)

task = Task(
    description="Criar um post para LinkedIn sobre otimização de custos AWS usando FinOps.",
    agent=linkedin_writer,
    expected_output="Post pronto para LinkedIn em português.",
)

crew = Crew(
    agents=[linkedin_writer, resume_optimizer, career_strategist],
    tasks=[task],
)

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
