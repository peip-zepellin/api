import network

class NetworkStation:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password

    def connect(self):
        self.station = network.WLAN(network.AP_IF)
        self.station.active(True)
        self.station.config(essid=self.ssid, password=self.password)

        print("Connection successful")
        print(self.station.ifconfig())

    def disconnect(self):
        self.station.disconnect()
        self.station.active(False)

network_station = NetworkStation('cacaprout', '12345678')

try:
    print('cc')
    network_station.connect()
except KeyboardInterrupt:
    network_station.disconnect()
