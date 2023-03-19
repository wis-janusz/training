import pytest

#List for problem 2
@pytest.fixture
def odd_list():
    return [4,1,6,1,73,6,45,4,2,8,6,2,4,5,9,71,3]

#User database for problem 4
@pytest.fixture
def user_db():
    return {'jwis':'hasło','wisj':'password','ktos_inny':'12345678'}

#Lists for problem 8
@pytest.fixture
def in_lists():
    return [[10, 20, 30], [40, 50, 60, 100], [70, 80, 90, 110]]

@pytest.fixture
def out_lists():
    return [[10,40,70],[20,50,80],[30,60,90],[100,110]]

