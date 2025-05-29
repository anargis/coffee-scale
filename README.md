# Coffee Scale 
The Coffee Scale is a DIY project built using a Raspberry Pi Pico and various electronic components. It measures coffee weight in real-time and displays the data on a small OLED screen. The goal of this project is to accurately track coffee quantity during consuming. [Watch the Coffee Scale Demo Video ](https://drive.google.com/file/d/1JX_wv30WXQk-MxV9DMYWIgs2iBv-3yjh/view?usp=drive_link)

### Installation
Python 
```
sudo apt install python3 -y
python3 --version
```

The PyPA recommended tool for installing Python packages.
```
sudo apt install python3-pip -y
pip3 --version

```

Tool for interacting remotely with MicroPython devices
```
pip3 install mpremote
mpremote --help
pip3 show mpremote
```

### Check if raspberry is detected as serial device
```ls /dev/ttyACM*```

### Connect
`mpremote connect /dev/ttyACM0 repl`

### Upload main file and libraries
```
mpremote connect /dev/ttyACM0 fs cp main.py :/main.py
mpremote connect /dev/ttyACM0 fs cp hx711.py :/hx711.py
mpremote connect /dev/ttyACM0 fs cp ssd1306.py :/ssd1306.py
```

### Reset
`mpremote connect /dev/ttyACM0 reset`

### Run
`mpremote connect /dev/ttyACM0 run main.py`

## Hardware
```
Raspberry Pi Pico 2 W - WiFi & Bluetooth 
Header Kit for Raspberry Pico - 20Pin x2 & 3Pin x1
OLED Module 0.96" 128x64 - I2C White 
Breadboard 400 Tie Point - White (Half-Size) 
HX711 (Soldered Header) 
Load Cell - 10kg 
Jumper Wires 30cm Female to Female
USB to Micro USB Power Cable
```

### Hardware Connection

##### OLED to Raspberry via Breadboard
```
GND  -> GND : Ground connection (common ground)	
VCC  -> 3V3(OUT) (I5 hole in the breadboard) : Power supply for the display (3.3V output from the Pico)	
SCL  -> GP5 : I²C Clock Line (SCL) - controls data flow	
SDA  -> GP4 : I²C Data Line (SDA) - transmits data	
```

##### HX711 to Raspberry via Breadboard
```
GND   -> GND : Common ground	
DT    -> GP16 : Data output from the HX711 to the Pico	
SCK   -> GP17 : Serial clock input to sync data	
VCC   -> 3V3(OUT) (J5 hole in the breadboard) : Power supply for the HX711 (3.3V from the Pico)	
```

##### HX711 to Load Cell
```
E+    -> red : Excitation voltage (+)	
E-    -> black : Excitation voltage (-)	
A-    -> white : Signal output (-)	
A+    -> green : Signal output (+)	

```