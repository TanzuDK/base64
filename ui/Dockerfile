# Stage 1: init
FROM python:3.11

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt --no-cache-dir
CMD ["python", "main.py"]