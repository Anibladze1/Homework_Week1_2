def main():
    file_name = input("Input File Name: ").strip().lower()
    unique = output_set(file_name)
    print(unique)


def output_set(file_name):
    unique_set = set()

    file = open(file_name)
    for line in file:
        unique_set.add(int(line))

    return unique_set


if __name__ == '__main__':
    main()
