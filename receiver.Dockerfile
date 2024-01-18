FROM python:3.10

RUN mkdir app
RUN useradd -ms /bin/bash admin
WORKDIR /app

COPY requirements.receiver.txt .
RUN pip install -r requirements.receiver.txt
COPY . .

RUN chown -R admin:admin /app
RUN chmod 755 /app
USER admin

CMD ["python", "src/receiver.py"]
