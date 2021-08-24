
def make_dict(number):
    """
    With a given integral number n, write a program to generate a dictionary that contains
    (i, i*i) such that is an integral number between 1 and n (both included). and then the program should
    print the dictionary.

    --> make_dict(8)
        {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
    """

    result_dict = {}
    for key in range(number):
        result_dict[key + 1] = (key + 1) * (key + 1)

    print("The resultant dictionary is writen below")
    print(result_dict)


if __name__ == '__main__':
    # print("Please enter the number")
    num = input("Please enter the number:   ")
    make_dict(int(num))
