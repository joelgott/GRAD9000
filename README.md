# Foobar

This repository contains all the contents for making and programming a Hal9000 type robot.

## Hardware

This robot uses a [seed studio XIAO ESP32-c3 development board](https://wiki.seeedstudio.com/XIAO_ESP32C3_Getting_Started/) with a [DFPlayer audio module](https://www.dfrobot.com/product-1121.html). 
In the hal9000mainboard folder there is a PCB that contains both boards, recieves a 5V input and has, a servo controller connector, an i2c bus output, a rgb led pinout and a speaker output. There is also a socket for an adxl345 accelerometer but the vcc and ground pins are swapped due to an error so it cannot be directly connected.

## Software

In the Circuitpython folder there is the code that runs on the robot.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

