def flip_string(test_string):

    
    
    n = len(test_string)

    if n == 1:
        return test_string
    return test_string[-1] + flip_string(test_string[:n-1])

string = '1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 1 1 1 1 1 1 1 1 1 1 0 0 1 0 0 1'
lst = list(map(int, string.split()))
print(len(lst))
