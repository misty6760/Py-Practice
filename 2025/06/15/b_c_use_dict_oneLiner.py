# 딕셔너리 연산
data = [('a', 1), ('b', 2), ('c', 3)]
dict_from_tuple = dict(data)
reversed_dict = {v: k for k, v in dict_from_tuple.items()}