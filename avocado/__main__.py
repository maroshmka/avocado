import logging
import logging.config

import avocado
from avocado.logger import LOGGING_CFG

if __name__ == '__main__':
    """Run as a module with `python3 -m avocado`"""
    logging.config.dictConfig(LOGGING_CFG)
    avocado.main()
