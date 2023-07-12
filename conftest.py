import pytest


@pytest.fixture(scope = "class")
def setup():
    print("I will execute first")
    yield
    print("I will execute last")

@pytest.fixture
def dataload():
    print("data being is created")
    return ("Hari","krishna","hari@gmail.com")