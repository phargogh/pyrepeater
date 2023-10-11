""" a simple repeater controller with periodic id """

import asyncio
import logging

from controller import Controller
from repeater import Repeater
from settings import ControllerSettings, RepeaterSettings

logger = logging.getLogger("pyrepeater")
logging.basicConfig(level=logging.INFO)


async def main():
    """main execution"""

    # repeater setup
    try:
        r_s = RepeaterSettings()
        rep = Repeater(r_s.serial_port, r_s)
    except Exception as err:
        logger.error("Unable to connect to repeater with error: %s", err)
        raise err

    # controller setup
    try:
        c_s = ControllerSettings()
        ctlr = Controller(rep, c_s)
    except Exception as err:
        logger.error("Unable to create controller with error: %s", err)
        raise err

    # start the controller
    try:
        await ctlr.start_controller()
    except KeyboardInterrupt:
        logger.info("Exiting")
        rep.close()
    except Exception as err:
        logger.error("Controller error: %s", err)
        raise err


if __name__ == "__main__":
    asyncio.run(main())
