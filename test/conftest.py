import pytest

#List for problem 2
@pytest.fixture
def odd_list():
    return [4,1,6,1,73,6,45,4,2,8,6,2,4,5,9,71,3]

#User database for problem 4
@pytest.fixture
def user_db():
    return {'jwis':'hasło','wisj':'password','ktos_inny':'12345678'}

