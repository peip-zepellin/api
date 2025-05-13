import machine
from packages.micropy_gps import MicropyGPS

class GPS:
    def __init__(self, pin_tx, pin_rx):
        self.pin_tx = pin_tx
        self.pin_rx = pin_rx
        self.serial = machine.UART(2, baudrate=9600, tx=self.pin_tx, rx=self.pin_rx)
        self.micropy_gps = MicropyGPS()

    def tick(self):
        try:
            while self.serial.any():
                data = self.serial.read()
                print(data)
                for byte in data:
                    stat = self.micropy_gps.update(chr(byte))
                    if stat is not None:
                        # Print parsed GPS data
                        print('UTC Timestamp:', self.micropy_gps.timestamp)
                        print('Date:', self.micropy_gps.date_string('long'))
                        print('Latitude:', self.micropy_gps.latitude_string())
                        print('Longitude:', self.micropy_gps.longitude_string())
                        print('Altitude:', self.micropy_gps.altitude)
                        print('Satellites in use:', self.micropy_gps.satellites_in_use)
                        print('Horizontal Dilution of Precision:', self.micropy_gps.hdop)
                        print()
                
        except Exception as e:
            print(f"Une erreur GPS est survenue: {e}")

    def get_data(self):
        return {
            'timestamp': self.micropy_gps.timestamp,
            'date': self.micropy_gps.date_string('long'),
            'latitude': self.micropy_gps.latitude_string(),
            'longitude': self.micropy_gps.longitude_string(),
            'altitude': self.micropy_gps.altitude,
            'satellites': self.micropy_gps.satellites_in_use,
            'horizontal_precision_dilution': self.micropy_gps.hdop,
        }
            

    def stop(self):
        pass

    def deinit(self):
        pass
