#!/usr/bin/env python3
#
# Created by: Rodas Nega
# Created on: Oct 2021
# This program uses two arrays with randomly generated numbers
#  and sorts them from least to greatest


import random


def rearrange_list(list_of_random_numbers_1, list_of_random_numbers_2):
    # this function finds the concatenates and sorts two arrays into one

    merged_numbers = []

    # process
    combined_numbers = list_of_random_numbers_1 + list_of_random_numbers_2

    while combined_numbers:
        min_value = combined_numbers[0]
        for x_value in combined_numbers:
            if x_value < min_value:
                min_value = x_value
        merged_numbers.append(min_value)
        combined_numbers.remove(min_value)

    return merged_numbers


def main():
    # this function uses two arrays to generate 10 random numbers
    #  from 1-100 and outputs the lists

    random_generated_numbers_1 = []
    random_generated_numbers_2 = []

    # output
    for loop_counter in range(0, 5):
        number_in_array_1 = random.randint(0, 100)
        number_in_array_2 = random.randint(0, 100)
        random_generated_numbers_1.append(number_in_array_1)
        random_generated_numbers_2.append(number_in_array_2)

    print(
        "When these lists concatenate: {0}  {1}".format(
            random_generated_numbers_1, random_generated_numbers_2
        )
    )

    ordered_list = rearrange_list(
        random_generated_numbers_1, random_generated_numbers_2
    )

    print("\nThe new ordered list is {0}.".format(ordered_list))
    print("\nDone.")


if __name__ == "__main__":
    main()
