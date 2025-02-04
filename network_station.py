import network

class NetworkStation:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password

    def connect(self):
        """
        self.station = network.WLAN(network.STA_IF)

        if self.station.isconnected() == True:
            print("Already connected")
            print(self.station.ifconfig())
            return

        self.station.active(True)
        self.station.connect(self.ssid, self.password)

        while self.station.isconnected() == False:
            print("Waiting for connection")
            pass

        print("Connection successful")
        print(self.station.ifconfig())
        """
        self.station = network.WLAN(network.AP_IF)
        self.station.active(True)
        self.station.config(essid=self.ssid, password=self.password)

        #while self.station.isconnected() == False:
        #    pass

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
