import logging


def insertion_sort(arr):
    """
    insertion_sort(arr) function reads integers prints them in sorted order using Insertion Sort
    :param arr: array contains integer values to be sorted
    :return: none
    """
    try:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1

            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j = j - 1

            arr[j + 1] = key

    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    arr1 = [9, 8, 6, 7, 1]
    print("Unsorted Array:", arr1)
    insertion_sort(arr1)
    print('Sorted Array: ', arr1)
