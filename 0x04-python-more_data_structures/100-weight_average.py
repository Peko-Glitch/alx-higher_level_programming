#!/usr/bin/python3
def weight_average(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return 0

    # Initialize variables for sum of products and sum of weights
    sum_product = 0
    sum_weights = 0

    # Calculate sum of products and sum of weights
    for score, weight in my_list:
        sum_product += score * weight
        sum_weights += weight

    # Calculate the weighted average
    weighted_avg = sum_product / sum_weights

    return weighted_avg
