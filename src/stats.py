"""Module that gives statistics functions for open formula """

#Import from Open Formula
from maths import __num_list_function


def MAX(*number_list):
    """Return the syntax for a maximum """
    return __num_list_function("MAX", *number_list)

def MIN(*number_list):
    """Return the syntax for a minimum """
    return __num_list_function("MIN", *number_list)

def AVERAGE(*number_list):
    """Return the syntax for an average """
    return __num_list_function("AVERAGE", *number_list)

def SUMPRODUCT(*number_list):
    """Return the syntax for a sumproduct """
    return __num_list_function("SUMPRODUCT", *number_list)
