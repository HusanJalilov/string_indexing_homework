def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """

    for a in range(5):
        if s[a]=="*":
            ans = a
        else:
            ans = "False"
    return ans
   
        

print(main("hus*a"))
            
        