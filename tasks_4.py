import operator


def sort_names():
    with open("sorted_names.txt", "w") as w:
        with open("./data/unsorted_names.txt", "r") as f:
            sorted_names = (f.readlines()).sort()
            sorted_names.sort()
            w.writelines(sorted_names)
            
def most_common_words(filepath, number_of_words=3):
    import string    
    with open(filepath, "r") as f:
        s = f.read().lower()
        s.translate(str.maketrans('', '', string.punctuation))
        all_words = s.split(" ")
        tmp_dict = {}
        for i in all_words:
            if i not in tmp_dict:
                tmp_dict[i] = 1
            else:
                tmp_dict[i] += 1
        result_list = []
        for i in range(number_of_words):
            most_common_word = max(tmp_dict.items(), key=operator.itemgetter(1))[0]
            result_list.append(most_common_word)
            tmp_dict.pop(most_common_word)
        return result_list


def get_top_performers(filepath, number_of_top_students=5):
    import csv
    with open(filepath, "r") as f:
        result_list = []
        reader = csv.DictReader(f)
        tmp_dict = {i["student name"]:i["average mark"] for i in reader}
        for i in range(number_of_top_students):
            most_common_word = max(tmp_dict.items(), key=operator.itemgetter(1))[0]
            result_list.append(most_common_word)
            tmp_dict.pop(most_common_word)
        return result_list


def sort_by_age(filepath):
    import csv
    with open(filepath, "r") as f:
        with open("sorted_students.csv", "w") as w:
            reader = csv.DictReader(f)
            sorted_dict = sorted(reader, key=lambda row: (row['age']), reverse=True)
            writer = csv.DictWriter(w, fieldnames=["student name", "age", "average mark"])
            writer.writeheader()
            writer.writerows(sorted_dict)


def remember_result(fun):
    result = None
    def wrapper(*args):
        print(f"Last result = {result}")
        fun(*args)
    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result       


def call_once(f):
    def wrapper(a, b):
        if not wrapper.has_run:
            result = f(a, b)
            wrapper.has_run = True
            return result
    wrapper.has_run = False
    return wrapper



@call_once
def sum_of_numbers(a, b):
    return a + b

'''
task 4.7
Такая ситуация происходит из-за того, что при импорте mod_b считывается сам модуль,
 а в нём находится переопределение переменной x, находящейся в модуле mod_c
'''
