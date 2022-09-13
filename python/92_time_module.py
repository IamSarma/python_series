import time

# time() function returns the total seconds passed between the
# UNIX epoch (12AM January 1 1970) and the moment time() was called 
print(time.time())


# Function that calculate the product of the first 100_000 numbers
def calcProd():
    prod_value = 1
    for i in range(1, 100_00):
        prod_value *= i
    return prod_value
