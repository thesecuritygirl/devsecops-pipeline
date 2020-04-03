FROM ubuntu:latest
RUN apt-get update -y \
  &&  apt-get install python3 python3-pip \
  &&  pip3 install flask pyyaml safety liccheck bandit
COPY  ./app.py /
CMD python3 /app.py
