# Traceback example
def callTest():
    test()


def test():
    raise Exception("This is the error message")


callTest()
