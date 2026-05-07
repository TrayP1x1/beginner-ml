import numpy as np

def create_array() -> np.ndarray:
    array = np.array([1, 2, 3, 4, 5], dtype=int)
    array += 10
    array *= 2

    return array


def create_matrix() -> np.ndarray:
    matrix = np.array(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    )

    print(f"Row 2: {matrix[1, :]}")
    print(f"Column 1: {matrix[:, 0]}")

    return matrix


def array_info(array: np.ndarray) -> None:
    print(f"The array is\n{array}")
    print(f"Shape: {array.shape}")
    print(f"dtype: {array.dtype}")
    print(f"Mean: {array.mean()}")


def array_mask(array: np.ndarray) -> None:
    mask = array > 24
    print(array)
    print(mask)
    print(array[mask])
    print(array[array > 28])


def main():
    # create_array()
    # create_matrix()
    # array_info(create_array())
    array_mask(create_array())


if __name__ == "__main__":
    main()
