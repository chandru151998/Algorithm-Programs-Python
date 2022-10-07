import logging


def binary_search(array, x, low, high):
    """
    binary_search(array, x, low, high) function is used to find the middle value in an array
    :param array: array contains integer values to be sorted
    :param x: value of the middle element in the array
    :param low: parameter low pointer is used to denote the smaller value
    :param high: parameter high pointer is used to denote the higher value
    :return: none
    """
    try:
        while low <= high:
            mid = low + (high - low) // 2
            if array[mid] == x:
                return mid
            elif array[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    array1 = [1, 5, 55, 25, 45, 50, 100, 9, 68]
    x1 = 50

    result = binary_search(array1, x1, 0, len(array1) - 1)

    if result != -1:
        print("Element is present at index " + str(result))
    else:
        print("Not found")
