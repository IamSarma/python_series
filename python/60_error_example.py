# Traceback example
import traceback

# def callTest():
#     test()


# def test():
#     raise Exception("This is the error message")


# callTest()

try:
    raise Exception("This is the error message")
except:
    error_file = open("error_info.txt", "w")
    error_file.write(traceback.format_exc())
    error_file.close()
    print("The traceback info was written to error_info.txt")
