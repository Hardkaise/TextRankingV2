#!/usr/bin/env python3

import sys

from src.file import read_file
from src.parser import parse
from src.parsing import error_argument
from src.parsing import is_dict_empty
from src.parsing import is_file_empty
from src.parsing import usage
from src.vector_space_model import tf_idf

if __name__ == '__main__':
    error_argument(len(sys.argv))
    usage(sys.argv[1])
    i = 1
    contents = list()
    while i < len(sys.argv) - 1:
        contents.append(read_file(sys.argv[i]))
        i += 1
    dicts = list()
    for content in contents:
        is_file_empty(content)
        dicts.append(parse(content))
    for dict1 in dicts:
        is_dict_empty(dict1)
    dicts.append(parse(sys.argv[len(sys.argv) - 1]))
    tf_idf(dicts, sys.argv)

