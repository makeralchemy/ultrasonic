# ultrasonic demonstration program

## Overview
*ultrasonic.py* is a Python program used to demonstrate how to use a HC-SR05 ultrasonic distance sensor on
a Raspberry Pi using Python.

*ultrasonic.py* will run under both Python 2 and Python 3.  It was tested on Python 2.7.13 and Python 3.5.3.

## Usage Instructions

*ultrasonic.py* is intended to be executed from the command line.

### Command Line Usage:

    $ python ultrasonic.py -h

    usage: ultrasonic.py [-h] [-a AVERAGED] [-i INDIVIDUAL] [-m MEASUREMENTS]

    optional arguments:
      -h, --help            show this help message and exit
      -a AVERAGED, --averaged AVERAGED
                            delay in seconds taking average measurements
      -i INDIVIDUAL, --individual INDIVIDUAL
                            delay in seconds between taking individual
                            measurements
      -m MEASUREMENTS, --measurements MEASUREMENTS
                            number of measurements for averaging

### Command Line Examples
Take measurements with the default values: 1 second delay between sets of averaged measurements,
1 measurement per averaged set, 1 second delay between indivual measurements.

     $ python ultrasonic.py

Take measurements with three second delay between sets of averaged measurements,
5 measurements to be averaged, 1/2 second delay between individual measurements.

     $ python ultrasonic.py -a 3.0 -m 5 -i 0.5

     or

     $python ultrasonic.py --averaged 3.0 --measurements 5 --individual 0.5

### Sample output

     $ python ultrasonic.py -a 3.0 -m 5 -i 0.5
     Number of measurements in each average:  5
     Delay between individual measurements:  0.5
     Delay between taking the averaged measurements:  3.0
     Ultrasonic Measurement
     Speed of sound is 331.12 m/s at  20 degrees celsius
     Measurement   1, Distance: 168.2
     Measurement   2, Distance: 168.2
     Measurement   3, Distance:  14.6
     Measurement   4, Distance:  13.8
     Measurement   5, Distance:  67.9
     Measurement   6, Distance:  38.1
     Measurement   7, Distance:  20.0
     Measurement   8, Distance:  20.9
     Measurement   9, Distance: 168.8
     ^C
     Keyboard Interrupt!
     $

## Installation Instructions

Create a directory for the program:

     mkdir ultrasonic
     cd ultrasonic

Install the monitor code:

     git clone https://github.com/makeralchemy/ultrasonic

After you have the Raspberry Pi setup, run the program:

     python ultrasonic.py

## License
This project is licensed under the MIT license.
