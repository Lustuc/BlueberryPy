# BlueberryPy
A python interface to control an Arduino UNO board. The ultimate goal is to control said board from a Rasberry Py using bluetooth (hence the name :p).

## Dependencies:
- Tkinter
- PyFirmata
- Python 3
\
(Above dependencies don't need to be fullfied if you only plan on using the executable)
- Arduino IDE

## Installation:

Unbuntu:
\
```sudo apt install -y python3 python3-pip```
\
```pip install pyFirmata```
\
```pip install tk```

ArchLinux:
\
```sudo pacman -S python python-pip```
\
```pip install pyFirmata```
\
```pip install tk```

By default, you might not have the required permissions to access /dev/ttyAMC0 (the board's port).
Run ```sudo gpasswd -a username tty``` to solve this issue permanently.

## Running:
First make sure ```SimpleDigitalFirmata.ino``` is uploaded to your board trough Arduino's IDE.
Then, while your board is connected to your computer, simply run ```python main.py``` or the ```Blueberry``` executable.

