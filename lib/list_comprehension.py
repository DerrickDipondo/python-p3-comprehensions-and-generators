#!/usr/bin/env python3

def return_evens(num_list):
    evens = [n for n in num_list if n%2 == 0]

    print(evens)

    return evens

return_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]