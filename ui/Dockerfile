# Stage 1: init
FROM python:3.11

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 8080
CMD ["python", "main.py"]