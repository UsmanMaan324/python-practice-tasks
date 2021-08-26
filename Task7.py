
def sort_words(words):
    """
    Write a program that accepts a comma separated sequence of words as input and prints
    the words in a comma-separated sequence after sorting them alphabetically.

    --> sort_words("without,hello,bag,world")
        bag,hello,without,world
    """
    word_list = [word for word in words.split(',')]
    word_list = sorted(word_list)

    [print(word, end=",") for word in word_list if word != word_list[-1]]
    print(word_list[-1])


if __name__ == '__main__':
    text = input("Enter the words with comma separated: ")
    sort_words(text)
