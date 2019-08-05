import numpy as np


def input_int(prompt, min=None, max=None):
    input_valid = False
    while not input_valid:
        try:
            number = int(input(prompt))
            if (min is None or number >= min) and (max is None or number <= max):
                input_valid = True
                return number
            else:
                if min is not None and max is not None:
                    print(f"Integers between {min} and {max} (inclusive) only!")
                elif min is not None:
                    print(f"Integers greater than or equal to {min} only!")
                else:
                    print(f"Integer less than or equal to {max} only!")
        except ValueError as e:
            print("Integers only!")


width = input_int("Width: ", 0, None)
height = input_int("Height: ", 0, None)
