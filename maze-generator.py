import numpy as np
import matplotlib.pyplot as plt


def input_int(prompt, default=None, min=None, max=None):
    input_valid = False
    while not input_valid:
        s = input(f"{prompt} (leave blank for {default}): ")
        try:
            x = int(s)
            if (min is None or x >= min) and (max is None or x <= max):
                input_valid = True
                return x
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

grid = np.ones((height, width))
grid[1, 3] = 0

plt.imshow(grid, cmap="gray_r", vmin=0, vmax=1)
plt.show()
