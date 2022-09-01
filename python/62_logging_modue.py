import logging
# # logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")
# logging.debug("Start of program")


# def factorial(n):
#     logging.debug(f"Start of factorial({n})")
#     total = 1
#     for i in range(1, n + 1):
#         total *= i
#         logging.debug(f"i is {str(i)}, total is {str(total)}")
#     logging.debug(f"End of factorial({n})")
#     return total


# print(factorial(5))
# logging.debug("End of program")


# Different level(s) of logging message(s)
logging.debug("Some debugging details")
logging.info("The logging module is working")
logging.warning("An error message is about to be logged")
logging.error("An error has occurred")
logging.critical("The program is unable to recover")
