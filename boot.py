# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import main

main.start()


"""

from hcsr04 import HCSR04
import time

sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=500*2*30) 

# Seuil de distance en cm
distance_threshold = 40
while True:
    # Mesure de la distance
    distance = sensor.distance_cm()
    print(distance, 'cm')
    time.sleep(2)
    
"""
    

"""
import machine
from time import sleep

gps_serial = machine.UART(2, baudrate=9600, tx=5, rx=18)

while True:
    print(gps_serial.any())
    if gps_serial.any():
        line = gps_serial.readline()  # Read a complete line from the UART
        if line:
            line = line.decode('utf-8')
            print(line.strip())
    sleep(0.5)
    
"""

