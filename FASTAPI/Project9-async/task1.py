# CALLBACK

# A function passed as an argument to another function and called later.

# Example 1

import time

def get_user_time(callback):
    time.sleep(2)
    callback("Krushna")

def print_user(name):
    print(name)

get_user_time(print_user)



# Example 2

def add(a, b, callback):
    result = a + b
    callback(result)

add(10, 20, print)