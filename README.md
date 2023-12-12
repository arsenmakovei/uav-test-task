# Drone Simulation

This project demonstrates the use of the Dronekit library 
to command a drone through a series of waypoints and actions. 
The script connects to a drone (or a simulated drone in SITL mode) 
and performs various flight operations

## Installation & Getting started

Python 3.6 must be already installed

1. Clone project and create virtual environment

```shell
git clone https://github.com/arsenmakovei/uav-test-task.git
cd uav-test-task
python -m venv venv
Windows: venv\Scripts\activate
Linux, Unix: source venv/bin/activate
pip install -r requirements.txt
pip uninstall pymavlink
pip install pymavlink==2.4.8
```

2. If you are a Windows user, you need to install 
[MAVProxy](https://ardupilot.org/mavproxy/docs/getting_started/download_and_installation.html)
3. Also, you need to install 
[Mission Planner](https://ardupilot.org/planner/docs/mission-planner-installation.html) 
for drone simulation

## How to Run

1. Mission Planner should be running
2. In separate terminals, run the following commands:

- Run dronekit copter
```shell
dronekit-sitl copter-3.3 --home=50.450739, 30.461242,584,383
```

- Run MAVProxy
```shell
# for Windows
mavproxy --master=tcp:127.0.0.1:5760 --out=udp:127.0.0.1:14550 --console
# for Linux
mavproxy.py --master=tcp:127.0.0.1:5760 --out=udp:127.0.0.1:14550
```

- Run the Python script
```shell
python main.py --connect udp:127.0.0.1:14550  
```

## Demo

Drone Simulation Video: https://clipchamp.com/watch/bZFZG2UPGi4
