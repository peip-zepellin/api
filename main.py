from distance_sensor import DistanceSensor
from motor_control import Motor
from gps_serial import GPS
from network_station import NetworkStation
from voltage_sensor import VoltageSensor
from web_server import WebServer
from machine import Pin

def start():
    # Configuration du pin où est connectée le ventilateur (ici le pin 18 est utilisé comme exemple)
    network_station = NetworkStation('Zeppelin', '1234567890')
    web_server = WebServer()

    gps = GPS(pin_tx=5, pin_rx=18)
    voltage_sensor = VoltageSensor(pin=Pin(32))
    distance_sensor = DistanceSensor(trigger_pin=5, echo_pin=18)
    motor1 = Motor(pin=Pin(12, Pin.OUT), debug=True)
    motor2 = Motor(pin=Pin(2, Pin.OUT), debug=True)
    motor3 = Motor(pin=Pin(14, Pin.OUT), debug=True)
    motor4 = Motor(pin=Pin(15, Pin.OUT), debug=True)

    web_server.add_component('gps', gps) # GPS
    web_server.add_component('voltage_sensor', voltage_sensor) # Voltage Sensor
    web_server.add_component('distance_sensor', distance_sensor) # Distance Sensor
    web_server.add_component('motor1', motor1) # Left
    web_server.add_component('motor2', motor2) # Right
    web_server.add_component('motor3', motor3) # Front
    web_server.add_component('motor4', motor4) # Brake

    try:
        motor1.set_speed(100)
        motor2.set_speed(100)
        motor3.set_speed(100)
        motor4.set_speed(100)

        network_station.connect()
        web_server.start()

        # Main Loop
        while True:
            print(voltage_sensor.get_voltage())
            gps.tick()
            web_server.tick()

    except KeyboardInterrupt:
        # Arrêter le PWM et éteindre le ventilateur en cas d'interruption
        network_station.disconnect()


