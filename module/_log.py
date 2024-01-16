import sys
from loguru import logger
from ._const import LOG_MODULE


logger.remove()

_format = "<green>[{extra[job]}]</green> <blue>{level}</blue> <green>{time:YYYY-MM-DD HH:mm:ss}</green> <yellow>{message}</yellow>"

logger.add(sys.stdout, level="INFO", format=_format, colorize=True)

# logger.add(LOG_MODULE, level='INFO', format=_format, filter=lambda x: x["extra"]["job"] == "module")
logger.add(LOG_MODULE, level='DEBUG', format=_format, filter=lambda x: x["extra"]["job"] == "module", backtrace=True, diagnose=True)


logger_module = logger.bind(job="module")

logger_rag = logger_module

