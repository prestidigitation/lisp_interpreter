import sys


def main(path_to_lisp_file):
    file = open_lisp_file(path_to_lisp_file)
    if file is None:
        sys.exit()

    for line in file.readlines():
        print(line)


def open_lisp_file(file_path):
    lisp_file = None
    try:
        lisp_file = open(file_path, 'r')
    except (OSError, IOError):
        print("Failed to open file!")
    return lisp_file


if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print("Invalid arguments")
        sys.exit()

    path_to_file = sys.argv[1]
    main(path_to_file)
