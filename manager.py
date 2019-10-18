import logging.handlers

import bluetooth

logger = logging.getLogger('kkdev_plugin_pybt')

handler = logging.handlers.SysLogHandler()
logger.addHandler(handler)


class javaConnector(object):

    def set_entrypoint(self, gateway, entry_point):
        self.entry_point = entry_point
        self.gateway = gateway

    def StartAdapter(self):
        logger.info("Receive command Start")

    def StopAdaper(self):
        logger.info("Receive command StopAdaper")

    def SetDiscoverableStatus(self):
        logger.info("Receive command setdiscostate")

    def State(self):
        logger.info("Receive command State")

    def RegisterService(self):
        logger.info("Receive command RegisterService")

    def SendJsonData(self):
        logger.info("Receive command SendJsonData")

    def RequestNearbyDevices(self):
        logger.info("RRNB")
        str_class = self.gateway.jvm.String
        item_arr = self.gateway.new_array(str_class, 2)

        ret = self.gateway.jvm.java.util.ArrayList()
        item = self.gateway.jvm.java.util.ArrayList()

        devs = bluetooth.discover_devices(15, True, True)
        for u, n in devs:
            item_arr[0] = u
            item_arr[1] = n
            ret.append(item_arr)
        logger.info("RRNB SEND " + ret)
        self.entry_point.ReceiveDeviceList(ret)
        logger.info("RRNB SEND OK")

    class Java:
        implements = ["kkdev.kksystem.plugin.bluetooth.adapters.bt_py.IBTAdapter_connector"]
