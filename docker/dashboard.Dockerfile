FROM python:3.12-slim

WORKDIR /app

COPY apps/dashboard/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY apps/dashboard /app

RUN useradd -u 10001 -m oracle
USER 10001

EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]
