Feature: Generating random numbers
        Testing generator

    Scenario: Generate with valid numbers
        Given Creating generator with 5 numbers
        When We receiving 5 numbers from generator
        Then Behave will test them for us
    Scenario: Generate with invalid numbers
        Given Creating generator
        When Trying to create generator getting error
        Then Checking if error occured
    Scenario: Check sort function
        Given Creating a list
        When Sorting the list
        Then Checking if list was sorted