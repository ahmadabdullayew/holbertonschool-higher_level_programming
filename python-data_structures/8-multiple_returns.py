#!/usr/bin/python3
def multiple_returns(sentence):
    first = None
    length = 0
    if sentence != "":
        first = sentence[0]
        length = len(sentence)
        print("Length: {:d} - First character: {}".format(length, first))
    else:
        print("Length: {:d} - First character: {}".format(length, first))
