"""Array indexing
"""
import numpy as np

def main():
    """Driven Function
    """
    arr_1d = np.arange(10)

    # Access the second element. Index notation
    print(arr_1d[1])
    # Last element
    print(arr_1d[-1])

    # Access 2D array elements
    arr_2d = np.array([[21, 22, 23, 24],
                       [31, 32, 33, 34],
                       [41, 42, 43, 44]])
    print("The 0,0 element \n", arr_2d[0, 0])
    print("The 2,-2 element \n", arr_2d[2, -2])
    print("Full first row \n", arr_2d[0])
    print("Full first Column \n", arr_2d[:, 0])

    # Slicing
    arr_1d = np.arange(10)
    print("All elements \n", arr_1d)
    print("Slicing elements 1:4 \n", arr_1d[1:4])
    print("Slicing elements 1:4:2 \n", arr_1d[1:4:2])


if __name__ == '__main__':
    main()