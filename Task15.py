def read_from_file(name):
    """
    Read data from file
    give the path as argument in this function

    --> read_from_file(path)
        return list separable by new line
    """
    file = open(name, 'r')
    text = file.read()
    file.close()

    return text.split('\n')


def count_names(names):
    """
    Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
     and print out the results to the screen.
    """
    result = {}
    for name in names:
        name_count = [t_name for t_name in names if t_name == name]
        result[name] = len(name_count)
    print(result)


if __name__ == '__main__':
    name_list = read_from_file("names.txt")
    count_names(name_list)
