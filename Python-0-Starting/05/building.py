import sys


def nbr_upperletters(object: str) -> int:
    '''This function takes a string as an argument
        and returns the number of upper letters in the string'''
    upper = 0
    for c in object:
        if (c.isupper()):
            upper += 1
    print(str(upper) + " upper letters")
    return 0


def nbr_lowerletters(object: str) -> int:
    '''This function takes a string as an argument
        and returns the number of lower letters in the string'''
    lower = 0
    for c in object:
        if (c.islower()):
            lower += 1
    print(str(lower) + " lower letters")
    return 0


def nbr_punctuationmarks(object: str) -> int:
    '''This function takes a string as an argument
        and returns the number of punctuation marks in the string'''
    punct = 0
    for c in object:
        if (c in ".,;:!?-"):
            punct += 1
    print(str(punct) + " punctuation marks")
    return 0


def nbr_spaces(object: str) -> int:
    '''This function takes a string as an argument
        and returns the number of spaces in the string'''
    spaces = 0
    for c in object:
        if (c.isspace() or c == "\n"):
            spaces += 1
    print(str(spaces) + " spaces")
    return 0


def nbr_digits(object: str) -> int:
    '''This function takes a string as an argument
        and returns the number of digits in the string'''
    digits = 0
    for c in object:
        if (c.isdigit()):
            digits += 1
    print(str(digits) + " digits")
    return 0


def nbr_chr(object: str) -> int:
    '''This function takes a string as an argument
        and returns the number of characters in the string'''
    print("The text contains " + str(len(object)) + " characters:")
    return 0


def str_composition(object: str) -> int:
    '''This function takes a string as an argument
        and returns the number of characters, upper letters,
        lower letters, punctuation marks, spaces
        and digits in the string.'''
    nbr_chr(object)
    nbr_upperletters(object)
    nbr_lowerletters(object)
    nbr_punctuationmarks(object)
    nbr_spaces(object)
    nbr_digits(object)
    return 0


def main():
    if (len(sys.argv) > 2):
        print("AssertionError: more than one argument is provided")
        return 1
    elif (len(sys.argv) < 2):
        print("What is the text to count?")
        object = sys.stdin.readline()
        str_composition(object)
        return 0
    else:
        str_composition(sys.argv[1])
        return 0


if (__name__ == "__main__"):
    main()
