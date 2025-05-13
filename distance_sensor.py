from packages.hcsr04 import HCSR04


class DistanceSensor:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        self.sensor = HCSR04(trigger_pin, echo_pin)

    def get_distance(self):
        return self.sensor.distance_cm()