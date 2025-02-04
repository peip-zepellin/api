from motor_control import Motor
from network_station import NetworkStation
from web_server import WebServer
import time
from machine import Pin

# Configuration du pin où est connectée le ventilateur (ici le pin 18 est utilisé comme exemple)
network_station = NetworkStation('Noacaca', '1234567890')
web_server = WebServer()

motor1 = Motor(pin=Pin(12, Pin.OUT), debug=True)
motor2 = Motor(pin=Pin(2, Pin.OUT), debug=True)
motor3 = Motor(pin=Pin(14, Pin.OUT), debug=True)

web_server.add_motor('motor1', motor1) # Left
web_server.add_motor('motor2', motor2) # Right
web_server.add_motor('motor3', motor3) # Front

print(0)

try:
    network_station.connect()
    web_server.start()

except KeyboardInterrupt:
    # Arrêter le PWM et éteindre le ventilateur en cas d'interruption
    network_station.disconnect()


