from bt.rfcomm_client import RFCOMM_Client
from bt.rfcomm_server import RFCOMM_Server


class BTService():
    def __init__(self, tag, name, addr, port, server_mode=False):
        self.service_tag = tag
        self.service_name = name
        self.service_addr = addr
        self.service_port = port
        self.server_mode = server_mode

        self.clients = {}

    def startService(self):
        if self.server_mode:
            self.server = RFCOMM_Server(self.service_name, self.service_tag, self.__register_connecton)
            self.server.start_listen(self.service_addr, self.service_port)
        else:
            client = RFCOMM_Client(self._data_receive)
            client.connect(self.service_addr, self.service_port)
            self.__register_connecton(client)


    def __register_connecton(self, connection):
        self.clients[connection.device_addr] = connection


    def _data_receive(self, addr, data):
        print(f"[PY_BT][DRCV]{addr} {data}")
