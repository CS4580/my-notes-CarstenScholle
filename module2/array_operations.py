"""Do array operations
"""
import numpy as np

def main():
    """Driven Function
    """
    numbers_lst = [2, 4, 6, 8, 10]
    print("Before adding 3: ", numbers_lst)

    # Increment each element by 3
    for i in range(len(numbers_lst)):
        numbers_lst[i] = numbers_lst[i] + 3
    
    print("After adding 3: ", numbers_lst)
    # Convert list to an Numpy array
    numbers_arr = np.array(numbers_lst)
    print("Before Array ", numbers_arr)
    numbers_arr += 3
    print("After Array ", numbers_arr)


if __name__ == '__main__':
    main()