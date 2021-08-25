import re


def find_patterns(str_list):
    """
    Write a Python program to remove the parenthesis area in a string.

    --> find_patterns(["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"])
        example
        w3resource
        github
        Stackoverflow
    """
    for str_element in str_list:
        pattern = re.sub(r"\w*\(\.\w*\)", "", str_element)
        print(pattern)


if __name__ == '__main__':
    text_list = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
    find_patterns(text_list)
