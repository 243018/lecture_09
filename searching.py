import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    file_path = os.path.join(cwd_path, file_name)

    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open(file_path, mode="r") as file:
        dictionary = json.load(file)

    return dictionary[field]


def linear_search(sequence, number):
    """
    linear search algorithm implementation
    :param sequence: (list), searched sequence
    :param number: (int), number to be found
    :return: (dict)
    """

    count = 0
    positions = []

    for i in range(len(sequence)):
        if sequence[i] == number:
            positions.append(i)
            count += 1

    return {
        "positions": positions,
        "count": count
    }


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    number = 5
    linear_result = linear_search(sequential_data, number)
    print(linear_result)


if __name__ == '__main__':
    main()