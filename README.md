# PV Simulator Challenge

This application models household consumption and electricity generation from solar panels.
The calculation difference between consumed and produced energy is recorded over time in a csv file, which is located in the results folder.

### When performing this task the following technologies were used:
* Python 3.10:
  * pika
  * pvlib
  * pytest
* RabbitMQ
* Docker
* Flake8
* Black

### Prerequisites
* Python 3.10+
* Docker 
* git

and run these commands in the terminal where the project is located:
```
git clone https://github.com/apostolovleks/PV_Simulator
```
```
cd PV_Simulator
```
create and activate virtual environment:
```
python -m venv venv

. venv/bin/activate
```
run docker compose:

```
sudo docker compose up
```
to stop a container:
```
sudo docker compose down
```
or Ctr+C.


To run tests you need to run the following commands:

```
pip install -r requirements.test.txt
```

Starting the RabbitMQ server if it is not running:
```
sudo docker compose up -d rabbitmq
```
Of course, in future tests, it will be necessary to replace the real server with a mock-server.

And then:
```
pytest
```
