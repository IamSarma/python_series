# Assert statement that triggers an AssertionError if variable is an integer less than 10
# final_score = 9
# assert int(final_score) >= 10


# Assert statement that triggers an AssertionError if two variables contains strings
# that are same as each other, even if their cases are different
# message_1 = "Hello"
# message_2 = "HeLlO"
# assert message_1.lower() != message_2.lower()


# Assert statement that always triggers an AssertionError
# is_eligible = False
# assert is_eligible


# Lines of code to enable logging
import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)s - %(levelname)s - %(message)s")
# logging.debug("This is a debug logging statement")


# To save logging to text file
# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)s - %(levelname)s - %(message)s",
#                     filename="log_to_text_file.txt")
# logging.debug("This is a debug logging statement")


# The 5 logging levels
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("This is a debug logging statement")
logging.info("This is a info logging statement")
logging.warning("This is a warning logging statement")
logging.error("This is a error logging statement")
logging.critical("This is a critical logging statement")
