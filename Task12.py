import re


def find_patterns(text):
    """
    Write a Python program to find urls in a string and output all urls as list.

    --> str = "My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles
                in the portal of http://www.geeksforgeeks.org"
    --> find_patterns(str)
        [https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles, http://www.geeksforgeeks.org]
    """
    pattern = re.compile(r"(https?://\S+)")
    matches = pattern.findall(text)
    print(matches)


if __name__ == '__main__':
    text_list = "My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles " \
                "in the portal of http://www.geeksforgeeks.org"

    find_patterns(text_list)
