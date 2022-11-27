def main():
    min_num = None

    for i in dictionary():
        if min_num is None or min_num > i:
            min_num = i

    print(min_num)


def dictionary():
    dict_input = {
        "one": 1,
        "two": 2,
        "ten": -10,
        "nine": 9,
        "twenty": 20,
        "three": 3,
    }

    x = dict_input.values()
    return x


if __name__ == '__main__':
    main()

