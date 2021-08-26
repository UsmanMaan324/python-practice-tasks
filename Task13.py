import time
import Task1
import Task2
import Task3


def calculate_execution_time(func):

    def wrapper(*args, **kwargs):
        """
        It will measure the time a function takes to execute and print the duration to the console
        """
        print("Name of task is ", func.__name__)
        start_time = time.time()
        func(*args, **kwargs)
        print("--- %s seconds ---" % (time.time() - start_time))
    return wrapper


@calculate_execution_time
def task1(num1, num2):
    Task1.sum_of_two_numbers(num1, num2)


@calculate_execution_time
def task2():
    Task2.find_divisible_by_7_not_5()


@calculate_execution_time
def task3(num):
    Task3.make_dict(num)


if __name__ == '__main__':
    task1(10, 10)
    print("------------------------------------------------------------")
    task2()
    print("------------------------------------------------------------")
    task3(5)

