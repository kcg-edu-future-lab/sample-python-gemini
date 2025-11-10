FROM python:3.14

RUN pip install -q -U google-genai fastapi uvicorn

WORKDIR /app
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
