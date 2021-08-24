
def square_odd_number_list(number_list):
    """
    Use a list comprehension to square each odd number in a list. The list is input
    by a sequence of comma-separated numbers.

    --> list = 1,2,3,4,5,6,7,8,9
    --> square_odd_number_list(list)
        1,9,25,49,81
    """
    temp_list = [int(num) for num in number_list.split(",")]
    temp_list = sorted(temp_list)
    ood_square_list = [(ood ** 2) for ood in temp_list if ood % 2 != 0]

    [print(num, end=",") for num in ood_square_list if num != ood_square_list[-1]]
    print(ood_square_list[-1])


if __name__ == '__main__':
    data = input("enter the element of list with comma separated:   ")
    square_odd_number_list(data)
