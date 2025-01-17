FROM python:3.12.8-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .


FROM python:3.12.8-slim 

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages/  /usr/local/lib/python3.12/site-packages/

COPY --from=builder /app/database.py /app
COPY --from=builder /app/main.py /app
COPY --from=builder /app/models.py /app
COPY --from=builder /app/routes.py /app

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "main:app","--host", "0.0.0.0", "--port", "8000"]