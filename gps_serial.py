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
            while serial.any():
                data = serial.read()
                print(data)
                for byte in data:
                    stat = micropy_gps.update(chr(byte))
                    if stat is not None:
                        # Print parsed GPS data
                        print('UTC Timestamp:', micropy_gps.timestamp)
                        print('Date:', micropy_gps.date_string('long'))
                        print('Latitude:', micropy_gps.latitude_string())
                        print('Longitude:', micropy_gps.longitude_string())
                        print('Altitude:', micropy_gps.altitude)
                        print('Satellites in use:', micropy_gps.satellites_in_use)
                        print('Horizontal Dilution of Precision:', micropy_gps.hdop)
                        print()
                
        except Exception as e:
            print(f"Une erreur GPS est survenue: {e}")
            

    def stop(self):
        pass

    def deinit(self):
        pass
