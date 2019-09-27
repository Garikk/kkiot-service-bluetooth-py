import threading

import bluetooth

class DataReader(threading.Thread):
    def __init__(self, rfcomm_client, data_receive):
        super().__init__()
        self.rfcomm_client = rfcomm_client
        self.data_receive = data_receive

    def run(self):
        self.active = True
        while (self.active):
            data = self.rfcomm_client.connection.recv(1024)
            self.data_receive(data)


class RFCOMM_Client():
    def __init__(self, data_receive):
        self.data_receive_callback=data_receive

    def accept_connection(self, sock):
        client_sock, address = sock.accept()
        self.device_addr = address
        self.connection=client_sock
        self._init_reader()

    def connect(self, addr, port):
        self.connection= bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        self.connection.connect((addr, port))
        self.device_addr = addr
        self._init_reader()

    def _init_reader(self):
        self.reader = DataReader(self, data_receive=self.data_receive)
        self.reader.start()

    def send_rfcomm_message(self, message):
        self.connection.send(message)

    def disconnect(self):
        self.reader.active = False
        self.connection.close()

    def data_receive(self, data):
        self.data_receive_callback(data)

