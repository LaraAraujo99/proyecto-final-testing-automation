import logging
import pathlib
from datetime import datetime
from logging.handlers import RotatingFileHandler

logs_dir = pathlib.Path("logs")
logs_dir.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")

handler = RotatingFileHandler(
    logs_dir /f"suite.log_{timestamp}",
    maxBytes= 100,
    backupCount= 5
)

logging.basicConfig(
    level= logging.INFO,
    handlers=[handler],
    format= "%(asctime)s %(levelname)s %(name)s - %(message)s",
    force= True
)

logger = logging.getLogger("talento_tech")
