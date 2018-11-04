from datetime import datetime
import logging.handlers
import sys

# Define log levels
LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

#Read command line arguments
cmdargs     = str(sys.argv)
scriptname  = sys.argv[0]
fileName, fileExt = str(sys.argv[0]).split(".")
logFileName = fileName + ".log"

if len(sys.argv) > 1:
    level       = LEVELS[sys.argv[1]]

else:
    level = LEVELS['info']

print ("Logging mode: ", level)

logger = logging.getLogger(__name__)
logger.setLevel(level)

#Create log file handler
handler = logging.handlers.RotatingFileHandler(logFileName, maxBytes=10485760, backupCount=3)

# create log file format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

#add handler to logger
logger.addHandler(handler)

logger.info('Program %s running', scriptname)
logger.info("fileName   : %s", fileName)
logger.info("logFileName: %s", logFileName)

#dt = datetime.fromtimestamp(datetime.today(), pytz.utc)
dt = datetime.now().date()
logger.info("dt         : %s", dt)

def linux_interaction(ID):
    assert ('linux' in sys.platform), "Run only on Linux systems."
    logger.info('Awsome Linux with input ID as ' + ID)

def osx_interaction(ID):
    assert ('darwin' in sys.platform), "Run only on OSX systems."
    logger.info('Awsome OSX with input ID as ' + ID.str())

try:
    logger.info("This line gets printed in INFO mode")
    logger.debug("This line gets printed in DEBUG mode")
    logger.warning("This line gets printed in WARNING mode")
    logger.error("This line gets printed in ERROR mode")
    osx_interaction(95)
    raise ValueError('Oops some thing bad with number calculations', 'arg1', 'arg2', 'arg3', 'arg4') 

except Exception as e:
    logger.critical("This line gets printed in Exception mode", exc_info=True)
    logger.error(e.args)
    raise

finally:
    logger.info("Program %s completed\n-----*****-----*****-----*****-----\n", scriptname)
