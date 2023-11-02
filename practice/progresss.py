import time

from progress.bar import Bar, ChargingBar

from logs import get_logger

logger = get_logger(__name__)


def get_progress_bar(data: list) -> None:
    logger.info("Started collecting data")
    bar = ChargingBar(message="Collecting data", max=len(data), suffix="%(percent)d%%")
    for item in data:
        # Do some stuff
        bar.next()
    bar.finish()
    logger.info("Finished collecting")
