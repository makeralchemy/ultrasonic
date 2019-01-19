#!/usr/bin/python

# This program is used to demonstrate how to use a
# HC-SR05 ultrasonic distance sensor.

# Import required Python libraries
from __future__ import print_function
import time
import RPi.GPIO as GPIO
import argparse

# Define GPIO pins for to be used for the sensor
GPIO_TRIGGER = 25
GPIO_ECHO = 24


def initialize_gpio(trigger_pin,
                    echo_pin,
                    ):

    """
    This function sets up the GPIO pins on the Raspberry Pi
    that are connected to the trigger and echo pins on the
    sensor.
    """

    # set GPIO mode to GPIO references rather than pin numbers
    GPIO.setmode(GPIO.BCM)

    # Set pins as output and input
    GPIO.setup(trigger_pin, GPIO.OUT)  # Trigger
    GPIO.setup(echo_pin, GPIO.IN)      # Echo


def initialize_sensor(trigger_pin,
                      echo_pin,
                      ):

    """
    This function initializes the ultrasonic distance
    sensor.
    """

    # Set trigger to False (Low)
    GPIO.output(trigger_pin, False)

    # Allow module to settle
    time.sleep(0.5)


def take_sensor_measurement(trigger_pin,
                            echo_pin,
                            ):

    """
    This function returns the elapsed time between
    the pulse and the echo.
    """

    # Send 10us pulse to trigger
    GPIO.output(trigger_pin, True)

    # Wait 10us
    time.sleep(0.00001)

    # Stop pulse
    GPIO.output(trigger_pin, False)

    start_time = time.time()

    while GPIO.input(echo_pin) == 0:
        start_time = time.time()

    while GPIO.input(echo_pin) == 1:
        stop_time = time.time()

    # Calculate pulse length
    elapsed_time = stop_time - start_time

    return elapsed_time


def get_average_measurement(trigger_pin,
                            echo_pin,
                            num_measurements,
                            delay,
                            ):
    """
    This function returns the average measurement of distance from the
    specified number of measurements.
    """

    measurement = 0.0
    for n in range(num_measurements):
        measurement += take_sensor_measurement(trigger_pin, echo_pin)
        time.sleep(delay)
    average_measurement = measurement / num_measurements
    return average_measurement


def monitor_ultrasonic_sensor(trigger_pin,
                              echo_pin,
                              measurements,
                              time_between_indiv_measurements,
                              time_between_avg_measurements,
                              ):

    """
    This function monitors the ultrasonic distance sensor and displays
    the measurements on the console.
    """

    # initialize the gpio pins and initialize the sensor.
    initialize_gpio(trigger_pin, echo_pin)
    initialize_sensor(trigger_pin, echo_pin)

    # Calculate the speed of sound in cm/s at room temperature.
    temperature = 20
    speed_of_sound = 33100 + (0.6 * temperature)

    print("Ultrasonic Measurement")
    print("Speed of sound is", speed_of_sound/100, "m/s at ",
          temperature, "degrees celsius")

    try:

        iteration = 0

        # Loop until a keyboard interrupt, take and display measurements.

        while True:

            iteration += 1

            elapsed = get_average_measurement(trigger_pin,
                                              echo_pin,
                                              measurements,
                                              time_between_indiv_measurements,
                                              )

            # Distance pulse travelled in that time is time multiplied by the
            # speed of sound (cm/s).
            distance = elapsed * speed_of_sound

            # That was the distance there and back so halve the value.
            distance = distance / 2

            print("Measurement %3d, Distance: %5.1f" % (iteration, distance))

            time.sleep(time_between_avg_measurements)

    except KeyboardInterrupt:

        # User pressed CTRL-C.
        print("\nKeyboard Interrupt!")

        # Reset GPIO settings.
        GPIO.cleanup()


if __name__ == "__main__":

    # Setup the command parser.
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--averaged", type=float, default=1.0,
                        help="delay in seconds taking average measurements")
    parser.add_argument("-i", "--individual", type=float, default=1.0,
                        help="delay in seconds between taking individual \
                        measurements")
    parser.add_argument("-m", "--measurements", type=int, default=1,
                        help="number of measurements for averaging")

    # Parse the command arguments.
    args = parser.parse_args()

    # Display the arguments.
    print("Number of measurements in each average: ", args.measurements)
    print("Delay between individual measurements: ", args.individual)
    print("Delay between taking the averaged measurements: ",
          args.averaged)

    # Start taking and displaying the distance measurements.
    monitor_ultrasonic_sensor(GPIO_TRIGGER,
                              GPIO_ECHO,
                              args.measurements,
                              args.individual,
                              args.averaged,
                              )
