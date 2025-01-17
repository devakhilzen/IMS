FROM python:3.12.8-slim AS builder

WORKDIR /app

COPY requirements2.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements2.txt

COPY . .

FROM python:3.12.8-slim 

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages/  /usr/local/lib/python3.12/site-packages/

COPY --from=builder /app/interface.py /app
COPY --from=builder /app/ims.png /app

EXPOSE 8501

CMD ["python", "-m", "streamlit", "run", "interface.py", "--server.port=8501", "--server.address=0.0.0.0"]