def main():
    file_name = input("Enter File Name: ")
    max_num = find_max(file_name)
    append_file(file_name, max_num)


def find_max(file_name):
    file = open(file_name, "r")
    max_num = int(file.readline())

    for line in file:
        if int(line) > int(max_num):
            max_num = line

    return max_num


def append_file(file_name, max_num):
    file = open(file_name, "a")
    file.write("\n"+max_num)


if __name__ == '__main__':
    main()

