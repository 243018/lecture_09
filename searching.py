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


def pattern_search(sequence, pattern):
    """
    sequential searching algorithm implementation
    :param sequence: (str), searched sequence
    :param pattern: (str), pattern to be found
    :return: (set), positions, where pattern was found within sequence
    """

    pattern_length = len(pattern)
    appearance = set()

    pattern_idx_left = 0
    pattern_idx_right = pattern_length


    while pattern_idx_right <= len(sequence):
        for idx_help in range(pattern_length):
            if sequence[pattern_idx_left + idx_help] != pattern[idx_help]:
                break
        else:
            appearance.add(pattern_idx_left + pattern_length // 2)

        pattern_idx_left += 1
        pattern_idx_right = pattern_idx_left + pattern_length

    return appearance


def binary_search(sequence, num):
    """
    binary search algorithm implementation
    :param sequence: (list), searched sequence
    :param num: (int), number to be found
    :return: (int), index where the number was found
    """

    left_idx = 0
    right_idx = len(sequence) - 1

    while left_idx <= right_idx:
        middle_idx = (left_idx + right_idx) // 2
        if sequence[middle_idx] == num:
            return middle_idx
        if sequence[middle_idx] > num:
            right_idx = middle_idx - 1
        elif sequence[middle_idx] < num:
            left_idx = middle_idx + 1

    return None


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    number = 5
    linear_result = linear_search(sequential_data, number)
    print(linear_result)

    pattern = "ATA"
    sequential_data2 = read_data("sequential.json", "dna_sequence")
    print(sequential_data2)
    pattern_result = pattern_search(sequential_data2, pattern)
    print(pattern_result)

    num = 13
    sequential_data3 = read_data("sequential.json", "ordered_numbers")
    binary_result = binary_search(sequential_data3, num)
    print(binary_result)


if __name__ == '__main__':
    main()
