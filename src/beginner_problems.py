from typing import List
from random import randint
from datetime import date
from collections import defaultdict
import getpass

#Problem 1: number guessing

def guess_number(max_n):
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

#Problem 2: mean, median and mode calculation

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

#Problem 3: password identification

def identify_password(user_db:dict):

    username_input = input('Podaj nazwę użytkownika: ')
    password_input = getpass.getpass('Podaj hasło: ')
    is_verified = 'Nieprawidłowa nazwa użytkownika lub hasło.'
    
    for user in user_db.keys():
        if user == username_input:
            for tries in range(3):
                if user_db[user] != password_input:
                    password_input = getpass.getpass('Podaj hasło ponownie: ')
                else:
                    is_verified = 'Zalogowano.'
                    break

    return is_verified

#Problem 5: Age calculation

def calculate_age(in_date_of_birth):
    date_of_birth = date.fromisoformat(in_date_of_birth)
    current_day = date.today()

    if (current_day-date_of_birth).days < 0:
        print('Nieprawidłowa data urodzenia, podaj datę wcześniejszą niż dziś.')
    else:
        age = current_day.year - date_of_birth.year
        if current_day.timetuple().tm_yday < date_of_birth.timetuple().tm_yday:
            age = age - 1
        print(f'Twój wiek to: {age}')

#Problem 6: Group anagrams

def group_anagrams(list_of_words):
    anagram_dict = defaultdict(list)
    for word in list_of_words:
        sorted_word = ''.join(sorted(word))
        print(sorted_word)
        anagram_dict[sorted_word].append(word)
    return anagram_dict

#Problem 7: Find missing number

def find_missing_numbers(in_array):
    missing_numbers = []
    for i in range(1,in_array[-1]):
        if i not in in_array:
            missing_numbers.append(i)
    
    return missing_numbers

#Problem 8: Group Elements of Same Indices

def group_same_indices(in_lists:list):
    max_i = max([len(x) for x in in_lists])
    out_lists = []
    for i in range(max_i):
        out_lists.append([])

    for sublist in in_lists:
         for i, element in enumerate(sublist):
             out_lists[i].append(element)

    return out_lists


