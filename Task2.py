
def find_divisible_by_7_not_5():
    """
    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 1000
    and 2000 (both included).
    """
    for i in range(1000, 2001):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=",")


if __name__ == '__main__':
    find_divisible_by_7_not_5()
