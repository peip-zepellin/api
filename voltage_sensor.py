from machine import ADC, Pin

class VoltageSensor:
    def __init__(self, pin, ref_voltage=3.3, adc_resolution=4095, r1=30000.0, r2=7500):
        self.ref_voltage = ref_voltage
        self.adc_resolution = adc_resolution
        self.r1 = r1
        self.r2 = r2
        self.pin = pin
        self.adc = ADC(pin)
        self.adc.atten(ADC.ATTN_11DB)  # Allow input voltage up to ~3.3V
        self.adc.width(ADC.WIDTH_12BIT)

    def get_voltage(self):
        adc_value = self.adc.read()

        voltage_adc = (adc_value * self.ref_voltage) / self.adc_resolution
        voltage_in = voltage_adc * (self.r1 + self.r2) / self.r2

        return voltage_in

    def stop(self):
        pass

    def deinit(self):
        pass