from math import pow, sqrt, log


def count_words(dict):
    nb = 0
    for value in dict:
        nb = nb + value[1]
    return nb


def create_vector(index: int, dicts: list):
    i = 0
    while i < len(dicts):
        if i != index:
            for value in dicts[i]:
                if value not in dicts[index]:
                    dicts[index][value] = 0
        i += 1
    return dicts[index]


def vector_multiplication(dict1: dict, query: dict):
    result = 0
    for k, v in dict1.items():
        result = result + v * query[k]
    return result


def norm_vector(vector: dict):
    result = 0
    for value in vector:
        result = result + pow(vector[value], 2)
    result = sqrt(result)
    return result


def idf(dicts: list, nb_document):
    idf_result = list()
    for k, v in dicts[len(dicts) - 1].items():
        i = 0
        nb_document_contain = 0
        if v != 0:
            while i < len(dicts) - 1:
                if dicts[i][k] > 0:
                    nb_document_contain += 1
                i += 1
            if nb_document_contain == 0:
                idf_result.append(log(nb_document / (1 + nb_document_contain)))
            else:
                idf_result.append(log(nb_document / nb_document_contain))
    return idf_result


def tf_idf(dicts: list, argv):
    vector_dict = list()
    i = 0
    while i < len(dicts):
        vector_dict.append(create_vector(i, dicts))
        i += 1
    i = 0
    result_tf = list()
    while i < len(vector_dict) - 1:
        result_tf.append(vector_multiplication(vector_dict[i], vector_dict[len(vector_dict) - 1]) /
                         (norm_vector(vector_dict[i]) * norm_vector(vector_dict[len(vector_dict) - 1])))
        i += 1
    ifd_result = idf(vector_dict, len(argv) - 2)
    results = list()
    for value in result_tf:
        result = 0
        for val in ifd_result:
            result = result + value * val
        results.append(result)
    print("Result for the query \"", argv[len(argv) - 1], "\":", sep='')
    i = 1
    for result in results:
        print(result, "-->", argv[i])
        i += 1
