# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:22 2022
@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants
Test task
"""

'''
    solution by: Polishchuk Orest (orest.polishchuk98@gmail.com)
    test task for Sierentz
'''


#simple function, wasn't tested
def get_sum_pair(S, data):
    '''
    s1, s2 = sum operands
    :param S: sum of 2 elems
    :param data: list of sorted nums
    :return: [xi,xj] both of which belong to data such that xi + xj = S
    '''
    index_1 = 0

    k = len(data)
    while index_1 < k:
        s1 = data[index_1]
        for index_inner in range(index_1 + 1, len(data)):
            if index_inner != len(data) and s1 + data[index_inner] == S:
                return [s1, data[index_inner]]
    index_1 += 1
    return [-1]

#function that uses two pointers
def get_sum_pair_2(S, data):
    '''
    s1, s2 = sum operands
    :param S: sum of 2 elems
    :param data: list of sorted nums
    :return: [xi,xj] both of which belong to data such that xi + xj = S    '''
    index_1 = 0
    index_2 = len(data) - 1

    while index_1 < index_2:
        if data[index_1] + data[index_2] < S:
            index_1 += 1
        elif data[index_1] + data[index_2] > S:
            index_2 -= 1
        elif data[index_1] + data[index_2] == S:
            return [data[index_1], data[index_2]]
    return [-1]

#function that uses hashmap
def get_sum_pair_3(S, data):
    """
    s1, s2 = sum operands
    :param S: sum of 2 elems
    :param data: list of sorted nums
    :return: [xi,xj] both of which belong to data such that xi + xj = S
    """
    s2_set = set()
    for index in range(len(data)):
        s1 = S - data[index]
        if s1 in s2_set:
            return [s1, data[index]]
        s2_set.add(data[index])
    return [-1]


if __name__ == "__main__":
    pair = get_sum_pair_2(10, [2, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18])
    pair_false = get_sum_pair_2(10, [1, 3, 8])
    pair_2 = get_sum_pair_3(10, [2, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18])
    pair_false_2 = get_sum_pair_3(10, [1, 3, 8])
    print(pair)
    print(pair_false)
    print(pair_2)
    print(pair_false_2)
