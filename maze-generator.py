import numpy as np


def input_int(prompt, default=None, min=None, max=None):
    input_valid = False
    while not input_valid:
        s = input(f"{prompt} (leave blank for {default}): ")
        try:
            number = int(s)
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
            if default is not None and s == "":
                return default
            else:
                print("Integers only!")


width = input_int("Width", 20, 0, None)
height = input_int("Height", width, 0, None)
