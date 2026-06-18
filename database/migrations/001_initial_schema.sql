-- Oracle Professional Intelligence — schema inicial
-- Memória estruturada (PostgreSQL) + memória semântica (pgvector).
-- Nota: embedding com dim 768 para casar com o modelo local nomic-embed-text
-- (Ollama). Se trocar para embeddings OpenAI/1536, ajuste a coluna e o índice.

CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS profiles (
    id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    headline TEXT,
    linkedin_url TEXT,
    github_url TEXT,
    target_roles TEXT,
    target_countries TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS linkedin_metrics (
    id SERIAL PRIMARY KEY,
    profile_id INTEGER REFERENCES profiles(id),
    ssi_score NUMERIC,
    professional_brand NUMERIC,
    find_right_people NUMERIC,
    engage_insights NUMERIC,
    build_relationships NUMERIC,
    collected_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT NOT NULL,
    topic TEXT,
    status TEXT DEFAULT 'draft',
    platform TEXT DEFAULT 'linkedin',
    published_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS comments (
    id SERIAL PRIMARY KEY,
    post_url TEXT,
    content TEXT NOT NULL,
    topic TEXT,
    status TEXT DEFAULT 'draft',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS recruiters (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    company TEXT,
    role TEXT,
    linkedin_url TEXT,
    country TEXT,
    status TEXT DEFAULT 'new',
    notes TEXT,
    next_follow_up DATE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS companies (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    website TEXT,
    linkedin_url TEXT,
    country TEXT,
    industry TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS jobs (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    company TEXT,
    location TEXT,
    remote BOOLEAN DEFAULT FALSE,
    salary_range TEXT,
    job_url TEXT,
    description TEXT,
    stack TEXT,
    match_score NUMERIC,
    status TEXT DEFAULT 'new',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS resumes (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT,
    target_role TEXT,
    target_company TEXT,
    language TEXT DEFAULT 'en',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS interviews (
    id SERIAL PRIMARY KEY,
    company TEXT,
    role TEXT,
    interview_type TEXT,
    questions TEXT,
    answers TEXT,
    feedback TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS content_calendar (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    topic TEXT,
    planned_date DATE,
    status TEXT DEFAULT 'planned',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS agent_runs (
    id SERIAL PRIMARY KEY,
    agent_name TEXT NOT NULL,
    input TEXT,
    output TEXT,
    status TEXT,
    started_at TIMESTAMP DEFAULT NOW(),
    finished_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS knowledge_documents (
    id SERIAL PRIMARY KEY,
    source TEXT,
    source_path TEXT,
    title TEXT,
    content TEXT,
    embedding vector(768),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Índices úteis
CREATE INDEX IF NOT EXISTS idx_jobs_status ON jobs(status);
CREATE INDEX IF NOT EXISTS idx_recruiters_status ON recruiters(status);
CREATE INDEX IF NOT EXISTS idx_posts_status ON posts(status);
CREATE INDEX IF NOT EXISTS idx_content_calendar_date ON content_calendar(planned_date);

-- Índice vetorial para busca semântica (cosine). ivfflat exige ANALYZE após
-- carga inicial; lists=100 é um ponto de partida razoável para volume pequeno.
CREATE INDEX IF NOT EXISTS idx_knowledge_embedding
    ON knowledge_documents
    USING ivfflat (embedding vector_cosine_ops)
    WITH (lists = 100);
