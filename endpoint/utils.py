import hashlib


def hash_string(my_string):
    h = hashlib.new('sha256')
    h.update(my_string.encode())
    return(h.hexdigest())

def is_palindrome_check(my_string):
    return my_string.lower() == my_string.lower()[::-1]

def character_map(my_string):
    my_dict = {}
    for i in my_string:
        try:
            if my_dict[i]:
                my_dict[i] += 1
        except KeyError:
            if i.isalpha():
                my_dict[i] = 1
    return my_dict

def word_counter(my_string):
    new_string = my_string.split()
    return len(new_string)

print(word_counter('fbnois bjkh kyfc sgj'))
print(is_palindrome_check('Aha'))
