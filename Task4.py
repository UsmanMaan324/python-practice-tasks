
class MyString:

    def __init__(self, text):
        self.text = text

    def get_string(self):
        """
        to get a string from console input
        """
        self.text = input("Please enter string: ")

    def print_string(self):
        """
        to print the string in upper case.
        """
        print(self.text.upper())


def test():
    """
    method to test the class function

    --> my_str = MyString("Hell Usman")
    --> my_str.print_string()
        Hello Usman
    """
    my_str = MyString("Hell Usman")
    my_str.print_string()
    my_str.get_string()
    my_str.print_string()


if __name__ == '__main__':
    test()
