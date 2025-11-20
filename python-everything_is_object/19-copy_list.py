#!/usr/bin/python3
def copy_list(a_list):
    """
    Return a shallow copy of the input list.

    Args:
        a_list (list): The list to be copied.

    Returns:
        list: A new list containing the same elements as a_list.

    Notes:
        - The copy is shallow, so mutable objects inside the list
          are shared between the original and the copy.
        - No modules are imported; slicing is used for copying.
    """
    return a_list[:]
