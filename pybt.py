import sys
import time
import logging
import logging.handlers
from py4j.java_gateway import JavaGateway, CallbackServerParameters
from daemon import Daemon
from manager import javaConnector

logging.basicConfig(filename="pybt_plugin.txt", level=logging.DEBUG)
logger = logging.getLogger('kkdev_plugin_pybt')
handler = logging.handlers.SysLogHandler()
logger.addHandler(handler)

class PyBT(Daemon):
    def run(self):
        try:
            java_connector = javaConnector()
            gateway = JavaGateway(
                callback_server_parameters=CallbackServerParameters(),
                python_server_entry_point=java_connector)
            java_connector.set_entrypoint(gateway, gateway.entry_point)
            while True:
                logger.info("Tick!")
                time.sleep(10)

        except Exception as ex:
            logger.critical(f"[BTPY][FAIL] {ex}")
            self.stop()


if __name__ == "__main__":
    daemon = PyBT('/tmp/pybt.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            logger.info("Start daemon")
            daemon.start()
        elif 'stop' == sys.argv[1]:
            logger.info("Stop daemon")
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            logger.info("Restart daemon")
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)
