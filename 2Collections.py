import random
from string import ascii_lowercase  # abcdefghijklmnopqrstuvwxyz


def generate_list_of_random_number_of_dicts():
    random_list = []
    # works with list, range from 1 to [2, 10]
    for i in range(1, random.randint(3, 11)):
        random_dict = {}
        # works with dict, range from 1 to [2, 5]
        for j in range(1, random.randint(3, 6)):
            # random letter as a key, random number from 1 to 100 as a value
            random_dict[(random.choice(ascii_lowercase))] = random.randint(1, 100)
        # add dict to list
        random_list.append(random_dict)
    return random_list


def create_aggregated_common_dict(list_to_be_aggregated: list):
    result_dict = {}
    # creates set with unique keys from generated list
    for k in set([j for i in list_to_be_aggregated for j in i]):
        # counts how many times was found needed key
        key_met_count = 0
        # value to be in result
        value = 0
        # dict number for key letter_N, where N - dict_number with max value
        dict_number = 0
        for i in list_to_be_aggregated:
            for j in i:
                # if found needed key
                if j == k:
                    key_met_count += 1
                    # if first time or value is bigger
                    if key_met_count == 1 or i[j] > value:
                        value = i[j]
                        dict_number = list_to_be_aggregated.index(i)
        # if key found one time, then key is letter_N(where letter = key, N - dict_number), else key = letter
        result_dict[k if key_met_count == 1 else k + '_' + str(dict_number + 1)] = value
    return result_dict


if __name__ == '__main__':
    # Task 1
    generated_list = generate_list_of_random_number_of_dicts()
    print(generated_list)

    # Task 2
    aggregated_dict = create_aggregated_common_dict(generated_list)
    print(aggregated_dict)
