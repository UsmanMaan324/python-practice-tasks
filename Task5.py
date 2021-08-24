
def make_all_capital(text):
    """Write a program that accepts string as input and prints the string after making
     all characters in the sentence capitalized.

     --> make_all_capital("hello")
        HELLO
     """

    print(text.upper())


if __name__ == '__main__':
    input_text = input("Enter the input string: ")

    make_all_capital(input_text)
