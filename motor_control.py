from machine import PWM

class Motor:
    def __init__(self, pin, freq=15000, min_duty=0, max_duty=1023, debug=False):
        self.pwm = PWM(pin)
        self.pwm.freq(freq)
        self.pin = pin
        self.min_duty = min_duty
        self.max_duty = max_duty
        self.debug = debug

        if self.debug:
            print('Motor at pin', pin, 'initialized with a frequence of', freq, 'Hz')
        
    def set_speed(self, speed=100):
        self.speed = speed
        self.pwm.duty(self.duty_cycle(self.speed))

        if self.debug:
            print('==== Motor', self.pin, '====')
            print('Speed:', speed)
            print('Duty Cycle:', self.duty_cycle(self.speed))
        
    def stop(self):
        self.speed = 0
        self.pwm.duty(0)
        
    def duty_cycle(self, speed):
        if speed <= 0 or speed > 100:
            duty_cycle = 0
        else:
            duty_cycle = int((self.max_duty - self.min_duty) * (speed / 100))
        return duty_cycle
    
    def deinit(self):
        self.pwm.deinit()
        self.pin.off()