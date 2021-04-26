FROM python:latest

RUN apt-get update -y

RUN apt-get install vim -y

RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata

RUN apt-get install openmpi-bin libopenmpi-dev rabbitmq-server -y

RUN pip install mpi4py rpyc pyzmq pika

CMD ['bash']
