FROM python:3.12-slim

WORKDIR /app

COPY apps/api/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY apps/api/src /app/src

# non-root (compatível com políticas Kyverno de runAsNonRoot)
RUN useradd -u 10001 -m oracle
USER 10001

EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
