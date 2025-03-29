# Use uma imagem Python como base
FROM python:3.10-slim

WORKDIR /FastApi
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]