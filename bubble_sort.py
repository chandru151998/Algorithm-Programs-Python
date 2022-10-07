import logging


def bubble_sort(list1):
    """
    bubble_sort(list1) function reads integers prints them in sorted order using Bubble Sort
    :param list1: list1 contains integer values to be sorted
    :return: none
    """
    try:
        for i in range(0, len(list1) - 1):
            for j in range(len(list1) - 1):
                if list1[j] > list1[j + 1]:
                    temp = list1[j]
                    list1[j] = list1[j + 1]
                    list1[j + 1] = temp
        return list1

    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    list2 = [5, 3, 8, 6, 7, 2]
    print("The unsorted list is: ", list2)
    print("The sorted list is: ", bubble_sort(list2))
