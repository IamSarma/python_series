def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character string")
    if width <= 2:
        raise Exception("Width must be greater than 2")
