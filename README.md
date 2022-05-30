# toyrobot

## Table of Contents
1. [Project Description](#general-info)
2. [Installation](#installation)
3. [How To Use?](#how)

### General Info
***
The Toy Robot is pyhton console application that simulates  a toy robot moving on a square tabe top of size 5x5. The robot accepts a set of commands in order to make a move.

## Installation
***
2.1. Pre requisite:
```
   Ensure that you have Docker engine installed on the host
```
2.2. Clone the toyrobot repo or download the zipped project:
```
$ git clone https://github.com/ndhambi/toyrobot
```
2.3. Use commnand/teminarl tool of choice to build a docker image of the toyrobot project:

```
$ docker build -t toyrobot .
```
2.4. Run the toy robot container from the image built in 2.3

```
$ docker run -it --name toyrobot toyrobot
```

 

## How To Use?
***
3.1. The container will launch in a command line to prompt user to enter commnands:
```
   Enter commnand:
```

NB: List commands that the application accepts:
```
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
```

3.2. The project contains a test module script (suite of tests) used to validate the application.The test can be perfomed by executing the following commands
```
  $ docker start robot
  $ docker exec -it {cotainer-id} /bin/bash 
```
 The above command will enable the bash of the container, then enter the following command in order to execute the test script:
 ```
  $ python3 test_robot.py 
