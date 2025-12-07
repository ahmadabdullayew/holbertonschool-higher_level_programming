#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    od_set = set.union(set_1, set_2) - set.intersection(set_1, set_2)
    return od_set
