"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    bake_time_remaining = EXPECTED_BAKE_TIME -  elapsed_bake_time
    return bake_time_remaining

def preparation_time_in_minutes(number_of_layers):
    '''
    Return Total preparation time.
    
    :param numbers_of_layers: int - total number of layers
    :return: int - total preparation time

    This function takes a number representing the number of layers & returns
    the output for total time required in preparation by multiplying it with time
    required for preparing a single layer. 
    '''
    preparation_time_in_minutes = number_of_layers*PREPARATION_TIME
    return preparation_time_in_minutes

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.
    
    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    elapsed_time_in_minutes = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return elapsed_time_in_minutes
