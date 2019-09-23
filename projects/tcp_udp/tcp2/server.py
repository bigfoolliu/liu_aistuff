import socketserver
import threading

ServerAddress = ("127.0.0.1", 6060)


class MyTCPClientHandler(socketserver.StreamRequestHandler):

    def handle(self):

        # Receive and print the data received from client
        print("Recieved one request from {}".format(self.client_address))
        msg = self.rfile.readline().strip()
        print("Data Recieved from client is:{}".format(msg))


# Create a Server Instance
TCPServerInstance = socketserver.ThreadingTCPServer(ServerAddress, MyTCPClientHandler)
# Make the server wait forever serving connections
TCPServerInstance.serve_forever()
