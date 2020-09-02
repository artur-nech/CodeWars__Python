#   You will have to create a function which takes in
#   a sequence of numbers in random order and
#   you will have to return the correct base of those numbers.

def base_finder(a):
    return int(max(x[-1] for x in a)) + 1

