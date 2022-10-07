import logging


def check(s1, s2):
    """
    check(s1, s2) function to checks if two strings are anagram or not
    :param s1: parameter s1 contains string
    :param s2: parameter s1 contains string
    :return: none
    """
    try:
        if sorted(s1) == sorted(s2):
            print("The strings are anagrams.")
        else:
            print("The strings aren't anagrams.")

    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    s11 = "listen"
    s22 = "silent"
    check(s11, s22)
