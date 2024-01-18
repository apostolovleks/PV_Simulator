FROM python:3.10

RUN mkdir app
WORKDIR /app

COPY requirements.producer.txt .
RUN pip install -r requirements.producer.txt

COPY . .

CMD ["python", "src/producer.py"]
