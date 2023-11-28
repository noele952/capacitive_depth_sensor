# Capacitive Depth Sensor Construction Guide

<p align="center">
  <img src="https://hydropi.s3.us-east-2.amazonaws.com/github/capacative_sensor/cap_sensor_complete.jpg" alt="Capacitive Depth Sensor" width="400" style="display: block; margin: 20 auto;">
</p>

Welcome to the world of Capacitive Depth Sensors! This repository is your hub for building the hardware and coding the brains behind a reliable depth sensor using a Pico microcontroller and MicroPython.

## Table of Contents

1. [Introduction](#introduction)
2. [Materials](#materials)
3. [Tools](#tools)
4. [Assembly](#assembly)
5. [MicroPython Code](#micropython-code)
6. [Calibration](#calibration)
7. [License](#license)

## Introduction

This guide provides step-by-step instructions on constructing a Capacitive Depth Sensor using simple materials.

The beauty of a capacitive sensor lies in its simplicity—no moving parts or additional electronics, except for the Pico microcontroller reading the sensor. We're just tapping into a fundamental physical characteristic of a metal rod.

The physical charactersitic we will be measuring is Capacitance. Capacitance is the ability of a component or circuit to collect and store energy in the form of an electrical charge. A capacitor works like a temporary storage tank for electrical energy. It consists of two conductive plates separated by an insulating material called a dielectric.

We will be creating a simple parallel plate capacitor by charging a metal rod and surrounding it with a grounded plate. The general equation governing the capacitance of a parallel plate capacitor is expressed as follows:

## $$C = \frac{\varepsilon \cdot A}{d}$$

Where:

- \( C \) is the capacitance.
- \( &epsilon; \) represents the absolute permittivity of the dielectric material
- \( A \) is the area of the capacitor plates.
- \( d \) signifies the separation between the capacitor plates.

Water has a higher dielectric constant compared to air.

- Air (or vacuum): Approximately 1 (for practical purposes, considered the baseline)
- Water: The dielectric constant of water varies, but it's roughly around 78 at room temperature.

The area and distance between the plates in our sensor will be set. But if we allow the central plate to be submerged in fluid, the absolute permitivity of the dielectric material, and thereby the Capacitance, will vary depending on the ratio of air and water.

In the code section we will connect the sensor to GPIO pins on a Pico W, and measure how long it takes to charge and discharge the capacitor. We will then collect this information at a variety of different depths, and use it to calibrate the sensor.

This is meant as a general guide; modify and adjust as necessary based on available materials. I've left out length measurements as that will vary based on the application.

## Materials

- PVC Pipe 1"
- PVC Pipe Endcaps (x2)
- PVC Pipe 1/2"
- 1/4" Silicone Tubing
- 1/4" Threaded Metal Rod (or unthreaded)
- Aluminum Foil
- Wires and connectors
- Silicone Adhesive

<p align="center">
<img src="https://hydropi.s3.us-east-2.amazonaws.com/github/capacative_sensor/cap_sensor_parts.jpg" alt="capacitive depth sensor parts" width="400" />
</p>

## Tools

To build this sensor you'll need tools to cut the PVC pipe to size, as well as the metal rod, and tubing. You will also need some kind of tool to put holes in the PVC pipe and endcaps

## Assembly

General principles to keep in mind. We cannot allow the fluid to come in contact with any of the metal parts of the senor. The submerged rod must be completely sealed, as well as the outer grounded plate. The portion of the sensor meant to hold the rod and the fluid must not be sealed at the top, air must be allowed to flow out of the top or it will not fill with fluid when submerged.

### Stage 1: Central Rod

<p align="center">
<img src="https://hydropi.s3.us-east-2.amazonaws.com/github/capacative_sensor/cap_sensor_rod.jpg" alt="capacitive depth sensor rod" width="400" />
</p>

The central part of the sensor is the steel rod which we will be getting charged, in this case a threaded steel rod. We will be connecting it to a GPIO pin on the Pico W.

Encase the rod in a length of silicone tubing, with a bit extra on either end.

<p align="center">
<img src="https://hydropi.s3.us-east-2.amazonaws.com/github/capacative_sensor/cap_sensor_rod_top.jpg" alt="capacitive depth sensor rod wiring" width="400" />
</p>

Attach the wire to the steel rod. In this case I stripped several inches of wire, tied it around the rod, and wrapped the rest around the threads of the rod before inserting it into the silicone tube. Seal the top with silicone.

<p align="center">
<img src="https://hydropi.s3.us-east-2.amazonaws.com/github/capacative_sensor/cap_sensor_rod_bottom.jpg" alt="capacitive depth sensor rod bottom" width="400" />
</p>

Fill the bottom end of the tube with silicone to seal it

### Stage 2: Metal Tube

<p align="center">
<img src="https://hydropi.s3.us-east-2.amazonaws.com/github/capacative_sensor/cap_sensor_tube.jpg" alt="capacitive depth sensor metal tube" width="400" />
</p>

To create the grounded metal tube to surround the charged rod, wrap the 1/4" PVC tube with aluminum foil. Apply a small amount of silicone adhesive to the edge of the foil, and roll it onto the tube so that it stays nice and tight.

<p align="center">
<img src="https://hydropi.s3.us-east-2.amazonaws.com/github/capacative_sensor/cap_sensor_tube_end.jpg" alt="capacitive depth sensor tube end" width="400" />
</p>

Before we wrap the tube we want to insert several inches of stripped wire between the foil and the PVC tube. Insert the stripped portion of the wire through the inside of the tube and seal it with a little silicone
The other end of the wire(not-stripped) will attach to ground on the Pico

## Stage 3: Insert Rod into Tube

<p align="center">
<img src="https://hydropi.s3.us-east-2.amazonaws.com/github/capacative_sensor/cap_sensor_rod_spacer.jpg" alt="capacitive depth sensor rod spacer" width="400" />
</p>

Before we insert the rod into the tube, we need to add some spacers to keep it centrally located within the tube. Take three short sections of tubing and split them up the side. Attach to the tubing with silicone adhesive, with equal spacing between them, alternating sides.

<p align="center">
<img src="https://hydropi.s3.us-east-2.amazonaws.com/github/capacative_sensor/cap_sensor_rod_into_tube.jpg" alt="capacitive depth sensor parts" width="400" />
</p>
Insert the rod into the tube, with the two wires together at the top. With the spacers on, it should fit snugly. Secure the top if the rod and the bottom of the rod with a little silicone adhesive. Make sure that you do not seal either end of the tube. Water must be able to flow in from the bottom, and air to flow out from the top.

## Stage 4: Outer Casing

<p align="center">
<img src="https://hydropi.s3.us-east-2.amazonaws.com/github/capacative_sensor/cap_sensor_attach_bottom.jpg" alt="capacitive depth sensor parts" width="400" />
</p>

Attach the bottom cap with silicone adhesive. Before installation drill a hole in the bottom of the cap, for the fluid to flow into the sensor. It is important that the cap and the tube are fully sealed, and aligned properly so that the outer PVC tube can slide down into the cap. We'll also want to apply spacers to the tube with silicone adhesive, as we did to the rod.

<p align="center">
<img src="https://hydropi.s3.us-east-2.amazonaws.com/github/capacative_sensor/cap_sensor_one_cap.jpg" alt="capacitive depth sensor parts" width="400" />
</p>

Slide the outer PVC tube down over the tube and into the cap. Apply silicone adhesive to seal the intersection between the tube and the lower cap.

<p align="center">
<img src="https://hydropi.s3.us-east-2.amazonaws.com/github/capacative_sensor/cap_sensor_top_cap.jpg" alt="capacitive depth sensor parts" width="400" />
</p>

The top cap has a small hole in the top to pass the wiring through, and a larger offset hole for airflow. Apply silicone adhesive to the joint between the cap and the PVC tube. Apply silicone adhesive to the wiring hole as well, to hold it securel to the cap.

<p align="center">
<img src="https://hydropi.s3.us-east-2.amazonaws.com/github/capacative_sensor/cap_sensor_complete.jpg" alt="capacitive depth sensor parts" width="400" />
</p>

The sensor is now complete. Just attach dupont connectors and it's ready to plug in

## Stage 5: Install Sensor

<p align="center">
<img src="https://hydropi.s3.us-east-2.amazonaws.com/github/capacative_sensor/cap_sensor_base.jpg" alt="capacitive depth sensor parts" width="400" />
</p>

For the base of the sensor mount, we're going to use a short piece of PVC pipe with a portion of the pipe removed. The base will make sure the hole at the bottom of the sensor is unobstructed.

<p align="center">
<img src="https://hydropi.s3.us-east-2.amazonaws.com/github/capacative_sensor/cap_sensor_base_installed.jpg" alt="capacitive depth sensor parts" width="400" />
</p>

Turn the opening in the base towards the edge of the bucket. to minimize the potential for any debris to get nto the senor. Place it so that the sensor, when placed on top, will lay flush with the bucket. Secure with silicon adhesive

<p align="center">
<img src="https://hydropi.s3.us-east-2.amazonaws.com/github/capacative_sensor/cap_sensor_installed.jpg" alt="capacitive depth sensor parts" width="400" />
</p>

Place the sensor on the base, and attach to the side of the bucket with silicone adhesive.

## MicroPython Code

### Sensor Data Monitoring

The MicroPython code for monitoring the sensor data can be found in the [capacitive_sensor.py](capacitive_sensor.py) file in this repository. It is designed to run on a Pico microcontroller. Adjust as needed for your application

```python
# Sample Python Code for Capacitive Depth Sensor Monitoring

charge_start_time = utime.ticks_us()
        charging_pin.value(1)
        charge_start_time = utime.ticks_us()
        if adc.read_u16() >= 65535 * .9:
            charge_time = utime.ticks_diff(utime.ticks_us(), charge_start_time)
            charging_pin.value(0)
            discharge_start_time = utime.ticks_us()
            while adc.read_u16() >= 65535 * .1:
                pass
            discharge_time = utime.ticks_diff(utime.ticks_us(), discharge_start_time)
            charge_time + discharge_time = charge_time + discharge_time
```

## Calibration

### Calibration Procedures

Locate a suitable container to submerge your depth sensor. Capture sensor readings at evenly spaced depth intervals. Calibrate the sensor based on your data.

The results will vary based on the specific parameters of the sensor(length, materials, etc.).

The details of my calibration are included in the attached Jupyter notebook

[capacitive_sensor_calibration](capacitive_sensor_calibration.ipynb)

### Calibration Points

| Time Constant (avg) | Known Fluid Level |
| ------------------- | ----------------- |
| 475 μs              | 0 cm              |
| 562 μs              | 5 cm              |
| 608 μs              | 10 cm             |
| 688 μs              | 15 cm             |
| 770 μs              | 20 cm             |
| 872 μs              | 25cm              |

### Calibration Curve Equation

The calibration curve is represented by the linear equation:

#### _depth = (cycle_time - 470) / 15.37_

## License

### Construction Guide

This construction guide is dedicated to the public domain under the [CC0 Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).

### Python Code

The Python code in this repository is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the [LICENSE](LICENSE) file for details.
