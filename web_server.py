import socket
import json

class WebServer:
    def __init__(self, ip='0.0.0.0', port=80):
        self.ip = ip
        self.port = port
        self.components = {}
        self.started = False

    def add_component(self, id, component):
        self.components[id] = component

    def start(self):
        self.address = socket.getaddrinfo(self.ip, self.port)[0][-1]
        self.server = socket.socket()
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(self.address)
        self.server.listen(512)

        print(f"Server running on {self.ip}:{self.port}")

        self.started = True

    def tick(self):
        if self.started:
            client, addr = self.server.accept()
            print(f"Client connected from {addr}")
            try:
                self.handle_client(client)
            except Exception as e:
                print(f"Error handling client: {e}")
            finally:
                client.close()

    def handle_client(self, client):
        data = client.recv(1024).decode('utf-8')
        if not data:
            return

        response = self.process_request(data)
        client.send(response.encode('utf-8'))

    def process_request(self, data):
        lines = data.split('\r\n')
        if not lines:
            return self.error_response(400, "Bad Request")

        request_line = lines[0].split()
        if len(request_line) < 3:
            return self.error_response(400, "Bad Request")

        method, path, _ = request_line
        route, _, query = path.partition('?')

        if route == '/ping':
            return self.success_response(200, json.dumps({ 'success': True }))
        elif route == '/motor-speed':
            return self.handle_motor_speed(query)
        elif route == '/gps-data':
            return self.handle_gps_data(query)
        else:
            return self.error_response(404, "Not Found")

    def handle_gps_data(self, query):
        params = self.parse_query_string(query)
        id_values = params.get('id', [])

        try:
            id = str(id_values[0])
        except ValueError:
            return self.error_response(400, "ID must be a string")

        if id not in self.components.keys():
            return self.error_response(400, f"The GPS {id} don't exist")

        gps = self.components[id]

        data = json.dumps(gps.get_data())

        return self.success_response(200, data)

    def handle_motor_speed(self, query):
        params = self.parse_query_string(query)
        speed_values = params.get('speed', [])
        id_values = params.get('id', [])

        if not speed_values:
            return self.error_response(400, "Missing speed parameter")

        try:
            speed = int(speed_values[0])
        except ValueError:
            return self.error_response(400, "Speed must be an integer")

        try:
            id = str(id_values[0])
        except ValueError:
            return self.error_response(400, "ID must be a string")

        if not 0 <= speed <= 100:
            return self.error_response(400, "Speed must be between 0-100")

        if id not in self.components.keys():
            return self.error_response(400, f"The motor {id} don't exist")

        self.components[id].set_speed(speed)

        # Add your motor control logic here
        return self.success_response(200, f"Motor {id} speed set to {speed}")

    def parse_query_string(self, query):
        params = {}
        if query:
            pairs = query.split('&')
            for pair in pairs:
                key, _, value = pair.partition('=')
                if key and value:
                    if key in params:
                        params[key].append(value)
                    else:
                        params[key] = [value]
        return params

    def success_response(self, code, message):
        return (
            f"HTTP/1.1 {code} OK\r\n"
            f"Content-Type: text/plain\r\n"
            f"Access-Control-Allow-Origin: *\r\n"
            f"Access-Control-Allow-Methods: GET, POST, OPTIONS\r\n"
            f"Access-Control-Allow-Headers: Content-Type\r\n"
            f"Content-Length: {len(message)}\r\n\r\n"
            f"{message}"
        )

    def error_response(self, code, message):
        return (
            f"HTTP/1.1 {code}\r\n"
            f"Content-Type: text/plain\r\n"
            f"Content-Length: {len(message)}\r\n\r\n"
            f"{message}"
        )

    def close(self):
        if self.server:
            self.server.close()
            print("Server stopped")
        for component in self.components.values():
            component.stop()
            component.deinit()


if __name__ == "__main__":
    server = WebServer()
    try:
        server.start()
    except KeyboardInterrupt:
        server.close()