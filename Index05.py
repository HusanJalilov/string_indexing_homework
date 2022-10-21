from curses.ascii import isdigit


def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    d=0
    for a in range(5):
        b=s[a]
        if b.isdigit():
            d+=1
    return d
print(main("12nhg"))