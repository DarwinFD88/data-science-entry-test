def string_reverse(s):
    #First I want to check if input for 's' is a string
    if type(s) == str:
    #If 's' is indeed a string, then I want to return 's' in reverse by slicing that starts from the end of the string; moves backward by -1 step
        return s[::-1]
    else:
    #If 's' is not a string; I want to print a message saying that 's' is not a string
        print('This is not a string')
        
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    return


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
string_reverse("Hello World")
string_reverse("Python")
