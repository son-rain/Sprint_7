import random
import string

import pytest


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@pytest.fixture(scope='function')
def generate_registration_data():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    data = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return data



