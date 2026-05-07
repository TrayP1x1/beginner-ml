import numpy as np


def create_array():
    array = np.array([1, 2, 3, 4, 5], dtype=int)
    array += 10
    array *= 2

    return array


def create_matrix():
    matrix = np.array(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    )

    print(f"Row 2: {matrix[1,:]}")
    print(f"Column 1: {matrix[:,0]}")

    return matrix


def array_info(array):

    print(f"The array is\n{array}")
    print(f"Shape: {array.shape}")
    print(f"dtype: {array.dtype}")
    print(f"Mean: {array.mean()}")


def main():
    create_array()
    create_matrix()
    array_info(create_array())


if __name__ == "__main__":
    main()
