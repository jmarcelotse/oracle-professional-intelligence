"""Cliente mínimo para o gateway LiteLLM (API compatível com OpenAI).

Usado pela API para gerar conteúdo (posts, mensagens) com os modelos locais
servidos via Ollama + LiteLLM.
"""
import os

import requests

LITELLM_BASE_URL = os.getenv("LITELLM_BASE_URL", "http://litellm.oracle-ai.svc.cluster.local:4000")
DEFAULT_MODEL = os.getenv("ORACLE_LLM_MODEL", "ollama/qwen2.5-coder:1.5b")


class LLMError(RuntimeError):
    pass


def chat(prompt: str, system: str | None = None, max_tokens: int = 400,
         temperature: float = 0.7, model: str | None = None) -> str:
    """Envia um prompt e devolve o texto da resposta."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    try:
        r = requests.post(
            f"{LITELLM_BASE_URL}/v1/chat/completions",
            json={
                "model": model or DEFAULT_MODEL,
                "messages": messages,
                "max_tokens": max_tokens,
                "temperature": temperature,
            },
            timeout=120,
        )
        r.raise_for_status()
        data = r.json()
        return data["choices"][0]["message"]["content"].strip()
    except requests.RequestException as exc:
        raise LLMError(f"LiteLLM request failed: {exc}") from exc
    except (KeyError, IndexError, ValueError) as exc:
        raise LLMError(f"unexpected LiteLLM response: {exc}") from exc
