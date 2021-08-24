
def count_letters_and_digits(text):
    """
    Write a program that accepts a sentence and calculate the number of letters and digits.

    --> count_letters_and_digits("hello world! 123")
        LETTERS 10
        DIGITS 3
    """

    digits = sum([char.isdigit() for char in text])
    letters = sum([char.isalpha() for char in text])

    print("LETTERS", str(letters))
    print("DIGITS", str(digits))


if __name__ == '__main__':
    input_text = input("Please enter the string:    ")
    count_letters_and_digits(input_text)
