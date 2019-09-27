from threading import Thread

import bluetooth

from bt.bt_device import BTDevice


class BTSocketWorkerClient(Thread):
    """
    A threading example
    """
    dev : BTDevice
    callback = None

    def __init__(self, bt_device : BTDevice, data_receive_callback):
        Thread.__init__(self)
        self.dev = bt_device
        self.callback  = data_receive_callback

    def run(self):
        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

        server_sock.connect((self.dev.addr, self.dev.port))
        client_sock, address = server_sock.accept()

        sck_open = True
        while sck_open:
            data = client_sock.readline()
            self.callback(self.dev, data)

        client_sock.close()
        server_sock.close()
