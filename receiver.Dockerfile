FROM python:3.10

WORKDIR /app

COPY requirements.receiver.txt .
RUN pip install -r requirements.receiver.txt
COPY . .

RUN chmod -R 777 ./src


CMD ["python", "src/receiver.py"]
