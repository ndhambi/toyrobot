FROM python:3

RUN mkdir /usr/src/robot
WORKDIR /usr/src/robot

COPY . .
CMD ["python","toyrobot.py"]