def printName(firstName, lastName, reverse):
    """
    Print name and you can also reverse
    test help(printName) to see the docstring
    """
    if reverse:
         print(lastName + ', ' + firstName)
    else:
         print(firstName, lastName)
