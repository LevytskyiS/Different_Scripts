import logging

# logging.basicConfig(level=logging.INFO, filename="practice/py_log.log",filemode="w",
#                     format="%(asctime)s %(levelname)s %(message)s")
# logging.debug("A DEBUG Message")
# logging.info("An INFO")
# logging.warning("A WARNING")
# logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")

# x_vals = [2,3,6,4,10]
# y_vals = [5,7,12,0,1]

# for x_val,y_val in zip(x_vals,y_vals):
#     x,y = x_val,y_val
#     logging.info(f"The values of x and y are {x} and {y}.")
#     try:
#         x/y
#         logging.info(f"x/y successful with result: {x/y}.")
#     except ZeroDivisionError as err:
#         logging.exception("ZeroDivisionError")


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    py_handler = logging.FileHandler(f"practice/my_project.log", mode="a")
    py_formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] - %(name)s - %(funcName)s(%(lineno)d) - %(message)s"
    )
    py_handler.setFormatter(py_formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(py_formatter)

    logger.addHandler(py_handler)
    logger.addHandler(stream_handler)

    return logger
