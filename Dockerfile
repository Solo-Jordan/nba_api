FROM python:3.11.3-buster

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

WORKDIR /app/src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]