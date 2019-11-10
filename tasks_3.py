from functools import reduce


def test_1_1(*strings):
    return reduce(lambda x, y: x.intersection(y), map(set, strings))


def test_1_2(*strings):
    return reduce(lambda x, y: x.union(y), map(set, strings))


def test_1_3(*strings):
    from itertools import combinations, starmap
    return set(map("".join, starmap(lambda x1, x2: x1.intersection(x2), combinations(map(set, strings), 2))))


def test_1_4(*strings):
    import string
    result = set(string.ascii_lowercase)
    for i in map(set, strings):
        result = result.difference(i)
    return result


def generate_squares(num):
    return {i:i**2 for i in range(1,num+1)}


def count_letters(string):
    return {i:string.count(i) for i in string}


def combine_dicts(*args):
    result_dict = {}
    for i in args:
        for k, v in i.items():
            if k not in result_dict:
                result_dict[k] = v
            else:
                result_dict[k] = result_dict[k]+i[k]
    return result_dict


if __name__ == "__main__":
    print(combine_dicts({'a':100}, {'a':100}))
