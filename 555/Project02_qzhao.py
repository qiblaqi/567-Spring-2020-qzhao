""" This is my simple docstring for the new spring semester """

def get_file():
    ""
    path = input("please type your file wtih the file path: ")
    my_file = open(path, "r")
    with my_file:
        lines = my_file.readlines()
        striped_lines = []
        for index, each_line in enumerate(lines):
            result = each_line.split()
            striped_lines.append(each_line.strip("\n"))
    return 1

def main():
    get_file()

if __name__ == '__main__':
    main()    