def error_argument(arg_size):
    if arg_size <= 3:
        print("Please enter a file in argument when you use this script.")
        exit(84)
    elif arg_size > 11:
        print("Error: Too much arguments.")
        exit(84)


def usage(argv):
    if argv == "--help":
        print("\nUSAGE:\n"
              "\t./text_ranking.py file1 file2 ... query\n"
              "\t./text_ranking.py --help\n\n"
              "\t\t--help display help\n"
              "\t\tfile1: a .txt filename\n"
              "\t\tfile2: a .txt filename\n"
              "\t\tquery: a string with some words\n")
        exit(0)


def is_file_empty(content):
    if content is None or len(content) == 0:
        print("Error: The file is empty.")
        exit(84)


def is_dict_empty(dict):
    if len(dict) == 0:
        print("Error: No words found")
        exit(84)
