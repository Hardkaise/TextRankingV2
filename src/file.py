from os.path import basename


def is_txt_file(file_name):
    base = basename(file_name)
    table = base.split('.')
    if table.__len__() <= 1 or table[1] != "txt":
        print("This is not a txt file, please enter .txt file.")
        exit(84)


def open_file(file_name):
    try:
        file = open(file_name, "r")
    except:
        print("Failed to open file, check name or permission.")
        exit(84)
    return file


def read_file(file_name):
    is_txt_file(file_name)
    file = open_file(file_name)
    content = file.read()
    file.close()
    return content
