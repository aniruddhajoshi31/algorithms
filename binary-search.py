def binary_search(array, item):

    # Initializing the low and high pointers
    low = 0
    high = len(array) - 1 # accounting for zero-based indexing

    while low <= high:

        # loop starts with adjusting the low and high pointers
        mid = (low + high)//2
        guess = array[mid]

        # Validity of the guess
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1

    # if the program could never get to return mid (exhausted search)
    return None


# Test
my_list = [1, 3, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
element = 27
result = binary_search(my_list, element)
print(result)

            
        

