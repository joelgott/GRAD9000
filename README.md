# Description

This project is strongly inspired by the HAL9000 robot from Stanley Kubrick's 2001 Space Odyssey. I used an ESP32 based board for the main logic and an audio module so that it looks like it's talking. Most of the mechanical parts are recicled or 3D printed.
This repository contains all the contents for making and programming the robot.

## Hardware

This robot uses a [seed studio XIAO ESP32-c3 development board](https://wiki.seeedstudio.com/XIAO_ESP32C3_Getting_Started/) with a [DFPlayer audio module](https://www.dfrobot.com/product-1121.html). 
In the PCB folder there is a custom designed PCB that contains both boards, recieves a 5V input and has, a servo controller connector, an i2c bus output, a rgb led pinout and a speaker output. There is also a socket for an adxl345 accelerometer and other audio output that can go to an amplifier.

## Software

In the Circuitpython folder there is the code that runs on the robot. There are two files, the one called eyetest lets me play with the rgb led to try animations and such. The other one called grad9000 contains the logic for controlling the audio module, reading the json file and switching the green led while maintaining the red one permanently on so that it looks like it's talking. 

## Extras

I also made a python script that lets you generate a json file that contains the information of the audio files. This json file can then be uploaded to the robot so it knows the duration of each audio file and how many are in each folder.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

