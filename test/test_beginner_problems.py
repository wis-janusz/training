from src import beginner_problems
import pytest
import statistics

# beginner_problems.number_guessing(20)

my_odd_list = [4, 1, 6, 1, 73, 6, 45, 4, 2, 8, 6, 2, 4, 5, 9, 71, 3]
my_even_list = my_odd_list[:-1]
one_mode_list = [0, 1, 2, 3, 4, 4, 5]
two_mode_list = [0, 1, 2, 3, 3, 4, 4, 5]
no_mode_list = [0, 1, 2, 3, 4, 5]
str_list = ["a", "b", "c"]


def test_median_odd(odd_list):
    expected_value = statistics.median(my_odd_list)
    assert beginner_problems.calc_median(odd_list) == expected_value


def test_median_wrong_type():
    in_list = my_even_list
    assert beginner_problems.calc_median(in_list) != 123


@pytest.mark.parametrize("in_list, expected", (([1, 2, 3], 2), ([4, 5, 6], 5)))
def test_with_parameter(in_list, expected):
    assert expected == beginner_problems.calc_median(in_list)


@pytest.mark.parametrize(
    "in_list, expected", (([1, 2, 3], 2), (["1", "2", "3"], TypeError))
)
def test_calc_mean_type(in_list, expected):
    """test mean"""
    try:
        result = beginner_problems.calc_mean(in_list)
        assert expected == result
    except TypeError:
        assert True

def test_identify_password_pass(user_db, monkeypatch):
    
    monkeypatch.setattr('builtins.input', lambda _: 'jwis')
    monkeypatch.setattr('getpass.getpass', lambda _: 'hasło')
    result = beginner_problems.identify_password(user_db)
    
    assert result == 'Zalogowano.'

def test_identify_password_pass_in3tries(user_db, monkeypatch):
    passwords = iter(['hasło','123da2342','12345678'])
    monkeypatch.setattr('builtins.input', lambda _: 'ktos_inny')
    monkeypatch.setattr('getpass.getpass', lambda _: next(passwords))
    result = beginner_problems.identify_password(user_db)
    
    assert result == 'Zalogowano.'

def test_identify_password_fail_user(user_db, monkeypatch):
    
    monkeypatch.setattr('builtins.input', lambda _: 'jwissss')
    monkeypatch.setattr('getpass.getpass', lambda _: 'hasło')
    result = beginner_problems.identify_password(user_db)
    
    assert result == 'Nieprawidłowa nazwa użytkownika lub hasło.'

def test_identify_password_fail_password(user_db, monkeypatch):
    
    monkeypatch.setattr('builtins.input', lambda _: 'wisj')
    monkeypatch.setattr('getpass.getpass', lambda _: 'hasło')
    result = beginner_problems.identify_password(user_db)
    
    assert result == 'Nieprawidłowa nazwa użytkownika lub hasło.'

def test_group_same_indices(in_lists, out_lists):
    result = beginner_problems.group_same_indices(in_lists)
    assert result == out_lists