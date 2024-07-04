import random


def create_list_with_random_int_values():
    result = []  # create list variable
    for i in range(0, 100):  # for loop, range from 0 to 99 (100 values)
        result.append(random.randint(1, 1000))  # fill the list with random values
    return result


def sort_using_selection_sort_algorithm(list_to_be_sorted: list):
    for i in range(len(list_to_be_sorted) - 1):
        min_i = i  # find minimum unsorted value
        for j in range(i + 1, len(list_to_be_sorted)):
            if list_to_be_sorted[min_i] > list_to_be_sorted[j]:
                min_i = j
        list_to_be_sorted[i], list_to_be_sorted[min_i] = list_to_be_sorted[min_i], list_to_be_sorted[i] # swap min value with first element
    return list_to_be_sorted


def calculate_avg_even_numbers(list_of_numbers: list):
    odd_numbers_list = [i for i in list_of_numbers if i % 2 == 0]  # filter even numbers
    return sum(odd_numbers_list) / len(odd_numbers_list)  # calculate avg value and return


def calculate_avg_odd_numbers(list_of_numbers: list):
    even_numbers_list = [i for i in list_of_numbers if i % 2 != 0]  # filter odd numbers
    return sum(even_numbers_list) / len(even_numbers_list)  # calculate avg value and return


if __name__ == '__main__':
    # create list of 100 random numbers from 0 to 1000
    list_100 = create_list_with_random_int_values()
    print('Created list with random values:', list_100)

    # sort list from min to max(without using sort())
    sorted_list = sort_using_selection_sort_algorithm(list_100)
    print('Sorted list:', sorted_list)

    # calculate average for even and odd numbers
    odd_avg = calculate_avg_odd_numbers(list_100)
    even_avg = calculate_avg_even_numbers(list_100)

    # print both average result in console
    print('Odd numbers avg:', odd_avg)
    print('Even numbers avg:', even_avg)
