from data_structures.hashtable import Hashtable


def left_join(a_table, b_table):
    combined_list = []

    for key, value in a_table.items():
        if b_table.get(key):
            combined_list.append([key, value, b_table.get(key)])
        else:
            combined_list.append([key, value, 'NONE'])


    return combined_list

