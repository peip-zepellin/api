from motor_control import Motor
from network_station import NetworkStation
from web_server import WebServer
import time
from machine import Pin

# Configuration du pin où est connectée le ventilateur (ici le pin 18 est utilisé comme exemple)
network_station = NetworkStation('cacaprout', '12345678')
web_server = WebServer()

motor1 = Motor(pin=Pin(12, Pin.OUT), debug=True)
motor2 = Motor(pin=Pin(2, Pin.OUT), debug=True)

web_server.add_motor('motor1', motor1)
web_server.add_motor('motor2', motor2)

print(0)

try:
    network_station.connect()
    web_server.start()

except KeyboardInterrupt:
    # Arrêter le PWM et éteindre le ventilateur en cas d'interruption
    network_station.disconnect()


