# This file represents your module.


# Random number generator:
def Random_n_g ():
    import numpy as np
    # Return list fith random integers from low (inclusive) to high (exclusive).
    number = np.random.randint(0, high=10, size=4, dtype=int)
    # Group the four elements in the list to a str
    strings = [str(num) for num in number]
    a_string = "".join(strings)
    # In the lines below we can modify number value to int (= int(a_string))
    # but remember int removes the left side ceros.
    number = (a_string)
    print(number)


