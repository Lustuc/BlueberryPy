# BlueberryPy
A python interface to control an Arduino UNO board. The ultimate goal is to control said board from a Rasberry Py using bluetooth (hence the name :p).

## Dependencies:
- Tkinter
- PyFirmata
- Python 3
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

## Running:
First make sure ```SimpleDigitalFirmata.ino``` is uploaded to your board trough Arduino's IDE.
Then, while your board is connected to your computer, simply run ```python main.py```.
