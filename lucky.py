# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:51 2022
@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants
Test task
"""

'''
    solution by: Polishchuk Orest (orest.polishchuk98@gmail.com)
    test task for Sierentz
'''


def check_lucky_series(series):
    """
    checks if a series of number is lucky
    :param takes a list series
    :return: true if the list is lucky, else false
    """
    if all([elem in [5, 6] for elem in series]) and (5 in series and 6 in series):
        return True
    else:
        return False


def get_lucky_series(series):
    '''
    computes lucky series and returns list of lucky series elements or 0 if none was found
    :param series: takes a list series
    :return: either 0 or list of lucky series elems
    '''
    lucky_elems = []
    index = 0
    k = len(series)
    while index < k:
        if series[index] in [5, 6]:
            elems = []
            elems.append(series[index])
            for index_inner in range(index + 1, len(series)):
                if index_inner != len(series) - 1 and series[index_inner] in [5, 6]:
                    elems.append(series[index_inner])
                elif index_inner != len(series) - 1 and series[index_inner] not in [5, 6]:
                    if check_lucky_series(elems) and len(elems) > len(lucky_elems):
                        lucky_elems = elems
                        index = index_inner
                        break
                    else:
                        index = index_inner
                        break

                elif index_inner == len(series) - 1:
                    if check_lucky_series(elems) and len(elems) > len(lucky_elems):
                        return elems
                    else:
                        return lucky_elems
        index += 1
    return lucky_elems if len(lucky_elems) > 0 else [0]


if __name__ == "__main__":
    list_1 = [5, 5, 1, 2, 3, 5, 6, 5, 6, 5, 5, 1, 2, 3]
    list_2 = [1, 2, 3]
    list_3 = [5, 5, 5, 5, 5, 1, 3, 2, 6, 5, 1, 1, 1, 2, 3, 4, 5, 1, 1, 5]
    longest_lucky = get_lucky_series(list_1)
    longest_lucky_2 = get_lucky_series(list_2)
    longest_lucky_3 = get_lucky_series(list_3)
    print(list_1, '--->', longest_lucky)
    print(list_2, '--->', longest_lucky_2)
    print(list_3, '--->', longest_lucky_3)
