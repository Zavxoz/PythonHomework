def replace_quotes(string):
    tmp_list = list(string)
    for i, el in enumerate(tmp_list):
        if el == '"':
            tmp_list[i] = "'"
        elif el == "'":
            tmp_list[i] = '"'
    return ''.join(tmp_list)

def check_palindrome(string):
    length = len(string)
    for i in range(length//2):
        if string[i]!=string[length-i]:
            return False
    return True

def split(string, separator):
    result_list = []
    index = 0
    prev_index = 0
    while True:
        index = string.find(separator)
        if index == -1:
            result_list.append(string)
            return result_list
        else:
            string = string[prev_index:index]
            result_list.append(string)
            prev_index = index
    return result_list


def split_by_index(string, indexes):
    indexes.reverse()
    index = indexes.pop()
    prev_index = 0
    result_list = []
    for i in indexes:
        result_list.append(string[prev_index:index])
        prev_index = index
        index = indexes.pop()
        if len(indexes) == 0:
            result_list.append(string[prev_index:index])
    result_list.append(string[index:])
    return result_list
        
def get_digits(num):
  return tuple(int(i) for i in str(num))

def get_longest_word(s):
    longest_word = ''
    for i in s:
        if i.isspace():
            tmp_list = s.split(i)
            if len(tmp_list[0])>len(longest_word):
                longest_word = tmp_list[0]
            get_longest_word(tmp_list[1])
    return longest_word


def foo(list_of_numbers):
    result_list = []
    import  functools
    mul = functools.reduce(lambda x1, x2: x1*x2, list_of_numbers)
    for i in list_of_numbers:
        if i == 0:
            result_list.append(mul)
        else:
            result_list.append(mul // i)
    return result_list


def get_pairs(lst):
   return  [(i, i+1) for i in lst if i+1]
    
        
    
