FROM python:3.12

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt --no-cache-dir

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
