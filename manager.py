import logging
import logging.handlers

logger = logging.getLogger('kkdev_plugin_pybt')

handler = logging.handlers.SysLogHandler()
logger.addHandler(handler)

class javaConnector(object):

    def __init__(self, java_callback):
        self.java_callback=java_callback

    def StartAdapter(self):
        logger.info("Receive command Start")
        self.java_callback.ReceiveData("tag","addr","data")
    def StopAdaper(self):
        logger.info("Receive command StopAdaper")
    def SetDiscoverableStatus(self):
        logger.info("Receive command SetDiscoverableStatus")
    def State(self):
        logger.info("Receive command State")
    def RegisterService(self):
        logger.info("Receive command RegisterService")
    def SendJsonData(self):
        logger.info("Receive command SendJsonData")

    class Java:
        implements = ["kkdev.kksystem.plugin.bluetooth.adapters.bt_py.IBTAdapter_connector"]


class javaCallback():
    def ReceiveData(self, ServiceTag, DeviceAddr, Data):
        logger.info("callback cmd")

    class Java:
        implements = ["kkdev.kksystem.plugin.bluetooth.adapters.bt_py.IBTAdapter_callback"]



