from random import random
from typing import List
from random import randint

def number_guessing(max_n):
    min_n = 0
    i_guess = 0
    x = randint(min_n,max_n)

    while True:
        i = int(input(f'Twoja liczba jest w zakresie [{min_n},{max_n}]. Zgadnij liczbę: '))
        if i == x:
            i_guess += 1
            print(f'Brawo! To jest twoja liczba! Ilość strałów: {i_guess}')
            break
        elif i < x:
            min_n = i+1
            i_guess += 1
            print(f'Niestety, to nie twoja liczba. Twoja liczba jest w zakresie [{min_n},{max_n}].')
        else:
            max_n = i-1
            i_guess += 1
            print(f'Niestety, to nie twoja liczba. Twoja liczba jest w zakresie [{min_n},{max_n}].')


def calc_mean(list_in: List[int]) -> float:
    if not all([int == type(x)for x in list_in]):
        raise TypeError
    
    temp_mean = 0
    
    for i in list_in:
        temp_mean += i
    
    out_mean = temp_mean / len(list_in)

    return out_mean

def calc_median(list_in):
    list_in.sort()
    if len(list_in)%2 == 0:
        mid_1 = list_in[len(list_in)//2 - 1]
        mid_2 = list_in[len(list_in)//2]
        median_out = (mid_1+mid_2)/2
    else:
        median_out = list_in[len(list_in)//2] 
    
    return median_out


def calc_mode(list_in):
    mode_out = []
    count_n = {}
    for i in list_in:
        count_n.setdefault(i,0)
        count_n[i] += 1

    most_frequent = max(count_n.values())
    for i, j in count_n.items():
        if j == most_frequent:
            mode_out.append(i)
    
    return mode_out

