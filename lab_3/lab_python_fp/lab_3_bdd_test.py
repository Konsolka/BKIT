import pytest
from pytest_bdd import scenario, given, when, then
from gen_random import gen_random
from random import randint
from sort import sort_py_abs

def configure_pytest():
    pytest.lst_gen_random = []

@scenario('test_bdd.feature', 'Generate with valid numbers')
def test_gen_with_valid_numbers():
    pass

@given("Creating generator with 5 numbers")
def step_impl():
    pytest.gen_random = gen_random(5, 1, 5)

@when("We receiving 5 numbers from generator")
def rec_n():
    pytest.lst_gen_random = list(pytest.gen_random)

@then("Behave will test them for us")
def no_error_message():
    assert len(pytest.lst_gen_random) == 5

@scenario("test_bdd.feature", "Generate with invalid numbers")
def test_gen_with_invalid_numbers():
    pass

@given("Creating generator")
def scinv_create_gen():
    pytest.gen_invalid_random = gen_random(5, 5, 1)

@when("Trying to create generator getting error")
def p():
    pass

@then("Checking if error occured")
def check_for_error():
    # Error will occure, i just don't know how to check it without unittest
    pass

@scenario("test_bdd.feature", "Check sort function")
def test_sort_function():
    pass

@given("Creating a list")
def create_unsorted_list():
    pytest.unsorted_lst = []
    for i in range(10):
        pytest.unsorted_lst.append(randint(1, 1000))

@when("Sorting the list")
def apply_sort_function():
    pytest.sorted_lst = sort_py_abs(pytest.unsorted_lst)

@then("Checking if list was sorted")
def check_sort_of_lst():
    temp_lst_sorted = sorted(pytest.unsorted_lst, key=abs,  reverse=True)
    for i, ii in zip(temp_lst_sorted, pytest.sorted_lst):
        assert i == ii
