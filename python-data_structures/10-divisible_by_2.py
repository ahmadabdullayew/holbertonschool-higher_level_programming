#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    list_result = []
    booleans = [True, False]
    for i in range(0, length):
        list_result.append(booleans[my_list[i] % 2])
    for i in range(0, length):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
