#Even First
#Your input is a list of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input list).
#Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def even_first(lst):
    # Initialize the left and right pointers
    left = 0
    right = len(lst) - 1

    # Iterate over the list until the left and right pointers cross
    while left < right:
        # Check if the left element is odd
        if lst[left] % 2 == 1:
            # Swap the left and right elements
            lst[left], lst[right] = lst[right], lst[left]

            # Move the right pointer one position to the left
            right -= 1

        # If the left element is even, move the left pointer one position to the right
        else:
            left += 1

    # Return the reordered list
    return lst
# Define a list of integers
lst = [7, 4, 5, 6, 2, 1, 3, 8,5,149,5,-13]

# Print the list with the even entries first
print(even_first(lst))