#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    r_value = list(a_dictionary.keys())[0]
    b_score = list(a_dictionary.values())[0]
    for o, i in a_dictionary.items():
        if i > b_score:
            b_score = i
            r_value = o
    return (r_value)
