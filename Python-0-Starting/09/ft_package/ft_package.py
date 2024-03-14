def count_in_list(object: list, str: str) -> int:
    '''Return the number of time the string str is in the list object'''
    return sum(1 for s in object if s == str)
