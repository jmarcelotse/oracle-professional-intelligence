"""Oracle Professional Intelligence — API.

API mínima porém funcional do MVP: health com checagem de banco, info do
projeto e CRUD básico de vagas, recrutadores e posts (memória estruturada).
"""
from typing import Optional

from fastapi import FastAPI, HTTPException
from psycopg.rows import dict_row
from pydantic import BaseModel

from . import db, llm

app = FastAPI(title="Oracle Professional Intelligence")

MODULES = [
    "LinkedIn Intelligence",
    "Career Intelligence",
    "Resume Intelligence",
    "Interview Intelligence",
    "Recruiter Intelligence",
    "Knowledge Intelligence",
]


@app.get("/")
def root():
    return {
        "project": "Oracle Professional Intelligence",
        "objective": "AI-powered professional intelligence platform",
        "modules": MODULES,
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "oracle-api",
        "database": "up" if db.check() else "down",
    }


# --------------------------------------------------------------------------- #
# Jobs
# --------------------------------------------------------------------------- #
class JobIn(BaseModel):
    title: str
    company: Optional[str] = None
    location: Optional[str] = None
    remote: bool = False
    salary_range: Optional[str] = None
    job_url: Optional[str] = None
    description: Optional[str] = None
    stack: Optional[str] = None
    match_score: Optional[float] = None
    status: str = "new"


@app.get("/jobs")
def list_jobs(status: Optional[str] = None, limit: int = 50):
    with db.cursor(row_factory=dict_row) as cur:
        if status:
            cur.execute(
                "SELECT * FROM jobs WHERE status = %s ORDER BY created_at DESC LIMIT %s",
                (status, limit),
            )
        else:
            cur.execute(
                "SELECT * FROM jobs ORDER BY created_at DESC LIMIT %s", (limit,)
            )
        return cur.fetchall()


@app.post("/jobs", status_code=201)
def create_job(job: JobIn):
    with db.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """INSERT INTO jobs
               (title, company, location, remote, salary_range, job_url,
                description, stack, match_score, status)
               VALUES (%(title)s, %(company)s, %(location)s, %(remote)s,
                       %(salary_range)s, %(job_url)s, %(description)s,
                       %(stack)s, %(match_score)s, %(status)s)
               RETURNING *""",
            job.model_dump(),
        )
        return cur.fetchone()


# --------------------------------------------------------------------------- #
# Recruiters
# --------------------------------------------------------------------------- #
class RecruiterIn(BaseModel):
    name: str
    company: Optional[str] = None
    role: Optional[str] = None
    linkedin_url: Optional[str] = None
    country: Optional[str] = None
    status: str = "new"
    notes: Optional[str] = None


@app.get("/recruiters")
def list_recruiters(limit: int = 50):
    with db.cursor(row_factory=dict_row) as cur:
        cur.execute(
            "SELECT * FROM recruiters ORDER BY created_at DESC LIMIT %s", (limit,)
        )
        return cur.fetchall()


@app.post("/recruiters", status_code=201)
def create_recruiter(rec: RecruiterIn):
    with db.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """INSERT INTO recruiters
               (name, company, role, linkedin_url, country, status, notes)
               VALUES (%(name)s, %(company)s, %(role)s, %(linkedin_url)s,
                       %(country)s, %(status)s, %(notes)s)
               RETURNING *""",
            rec.model_dump(),
        )
        return cur.fetchone()


# --------------------------------------------------------------------------- #
# Posts
# --------------------------------------------------------------------------- #
class PostIn(BaseModel):
    title: Optional[str] = None
    content: str
    topic: Optional[str] = None
    status: str = "draft"
    platform: str = "linkedin"


@app.get("/posts")
def list_posts(status: Optional[str] = None, limit: int = 50):
    with db.cursor(row_factory=dict_row) as cur:
        if status:
            cur.execute(
                "SELECT * FROM posts WHERE status = %s ORDER BY created_at DESC LIMIT %s",
                (status, limit),
            )
        else:
            cur.execute(
                "SELECT * FROM posts ORDER BY created_at DESC LIMIT %s", (limit,)
            )
        return cur.fetchall()


@app.post("/posts", status_code=201)
def create_post(post: PostIn):
    with db.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """INSERT INTO posts (title, content, topic, status, platform)
               VALUES (%(title)s, %(content)s, %(topic)s, %(status)s, %(platform)s)
               RETURNING *""",
            post.model_dump(),
        )
        return cur.fetchone()


# --------------------------------------------------------------------------- #
# Intelligence — geração de conteúdo via LiteLLM (modelos locais)
# --------------------------------------------------------------------------- #
class GeneratePostIn(BaseModel):
    topic: str
    language: str = "pt-BR"
    tone: str = "profissional e técnico"
    save: bool = True


@app.post("/generate/post")
def generate_post(req: GeneratePostIn):
    """Gera um rascunho de post de LinkedIn e (opcional) salva como draft."""
    system = (
        "Você é um especialista em DevOps, SRE, Cloud e FinOps que escreve "
        "posts de LinkedIn envolventes para uma audiência técnica. "
        f"Escreva no idioma {req.language}, com tom {req.tone}. "
        "Inclua um gancho inicial, 2-3 parágrafos curtos, e termine com "
        "3 a 5 hashtags relevantes."
    )
    try:
        content = llm.chat(f"Tema do post: {req.topic}", system=system, max_tokens=900)
    except llm.LLMError as exc:
        raise HTTPException(status_code=502, detail=str(exc))

    result = {"topic": req.topic, "language": req.language, "content": content}
    if req.save:
        with db.cursor(row_factory=dict_row) as cur:
            cur.execute(
                """INSERT INTO posts (title, content, topic, status, platform)
                   VALUES (%s, %s, %s, 'draft', 'linkedin') RETURNING id""",
                (req.topic, content, req.topic),
            )
            result["post_id"] = cur.fetchone()["id"]
    return result


class GenerateOutreachIn(BaseModel):
    recruiter_name: str
    company: str
    target_role: str
    language: str = "en"


@app.post("/generate/outreach")
def generate_outreach(req: GenerateOutreachIn):
    """Gera uma mensagem curta de conexão/apresentação para um recrutador."""
    system = (
        "Você escreve mensagens curtas, calorosas e profissionais para "
        f"recrutadores no LinkedIn, no idioma {req.language}. Máximo 4 frases, "
        "sem soar genérico, com um CTA leve."
    )
    prompt = (
        f"Recrutador: {req.recruiter_name}. Empresa: {req.company}. "
        f"Cargo de interesse: {req.target_role}."
    )
    try:
        content = llm.chat(prompt, system=system, max_tokens=200)
    except llm.LLMError as exc:
        raise HTTPException(status_code=502, detail=str(exc))
    return {"message": content}


# --------------------------------------------------------------------------- #
# Ingestão em lote (usada pela automação n8n — e-mails do LinkedIn etc.)
# Idempotente: não duplica.
# --------------------------------------------------------------------------- #
class JobsIngestIn(BaseModel):
    jobs: list[JobIn]


@app.post("/jobs/ingest")
def ingest_jobs(payload: JobsIngestIn):
    """Insere várias vagas, pulando as que já existem (dedup por job_url)."""
    created, skipped = 0, 0
    with db.cursor() as cur:
        for job in payload.jobs:
            if job.job_url:
                cur.execute("SELECT 1 FROM jobs WHERE job_url = %s", (job.job_url,))
                if cur.fetchone():
                    skipped += 1
                    continue
            cur.execute(
                """INSERT INTO jobs
                   (title, company, location, remote, salary_range, job_url,
                    description, stack, match_score, status)
                   VALUES (%(title)s, %(company)s, %(location)s, %(remote)s,
                           %(salary_range)s, %(job_url)s, %(description)s,
                           %(stack)s, %(match_score)s, %(status)s)""",
                job.model_dump(),
            )
            created += 1
    return {"created": created, "skipped": skipped}


class RecruitersIngestIn(BaseModel):
    recruiters: list[RecruiterIn]


@app.post("/recruiters/ingest")
def ingest_recruiters(payload: RecruitersIngestIn):
    """Insere recrutadores, pulando duplicados (por linkedin_url ou nome+empresa)."""
    created, skipped = 0, 0
    with db.cursor() as cur:
        for rec in payload.recruiters:
            if rec.linkedin_url:
                cur.execute("SELECT 1 FROM recruiters WHERE linkedin_url = %s", (rec.linkedin_url,))
            else:
                cur.execute(
                    "SELECT 1 FROM recruiters WHERE name = %s AND coalesce(company,'') = %s",
                    (rec.name, rec.company or ""),
                )
            if cur.fetchone():
                skipped += 1
                continue
            cur.execute(
                """INSERT INTO recruiters
                   (name, company, role, linkedin_url, country, status, notes)
                   VALUES (%(name)s, %(company)s, %(role)s, %(linkedin_url)s,
                           %(country)s, %(status)s, %(notes)s)""",
                rec.model_dump(),
            )
            created += 1
    return {"created": created, "skipped": skipped}


@app.get("/stats")
def stats():
    """Contadores para o dashboard."""
    queries = {
        "jobs": "SELECT count(*) FROM jobs",
        "recruiters": "SELECT count(*) FROM recruiters",
        "posts": "SELECT count(*) FROM posts",
        "resumes": "SELECT count(*) FROM resumes",
        "interviews": "SELECT count(*) FROM interviews",
    }
    out = {}
    try:
        with db.cursor() as cur:
            for key, q in queries.items():
                cur.execute(q)
                out[key] = cur.fetchone()[0]
    except Exception as exc:  # banco indisponível
        raise HTTPException(status_code=503, detail=f"database unavailable: {exc}")
    return out
