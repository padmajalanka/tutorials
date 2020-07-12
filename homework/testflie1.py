"""
    this is home work for testing a function which returns a boolean value

"""


def bool_check_function():
    a = 30
    b = 10
    ret_value = False
    if a > b:
        ret_value = True
    else:
        ret_value = False
    return ret_value


junk_value = bool(bool_check_function())
print(junk_value)
