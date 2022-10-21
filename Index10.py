def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    m=0
    for a in range(5):
        if s[a].isdigit():
            m+=int(s[a])
    

    return m
print(main("1kk12"))