import re


def validate_password(password_string):

    pattern = re.compile(r'(?=.*[@$#])(?=.*[a-z])(?=.*[A-Z])(?=.*\d)')
    passwords = [password for password in password_string.split(',')]

    for password in passwords:
        if 13 > len(password) > 5:
            match = pattern.match(password)
            if match:
                print(password)


if __name__ == '__main__':
    input_str = "ABd1234@1,a F1#,2w3E*,@We3#45,12aQ5678"
    validate_password(input_str)
