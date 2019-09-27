import bluetooth

from bt.rfcomm_client import RFCOMM_Client


class RFCOMM_Server():
    def __init__(self, service_name, service_tag, connection_callback, data_receive_callback):
        self.service_name = service_name
        self.service_tag = service_tag
        self.connection_callback=connection_callback
        self.data_receive_callback = data_receive_callback

    def start_listen(self, port, addr=""):
        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_sock.bind((addr, port))
        self.active = True
        while (self.active):
            server_sock.listen(1)
            client = RFCOMM_Client(self.data_receive_callback)
            client.accept_connection(server_sock)
            self.connection_callback(client)

        server_sock.close()
