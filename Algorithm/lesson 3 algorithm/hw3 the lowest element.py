#Two Lowest Elements
#When given a list of elements, find the two lowest elements.
#They can be equal to each other or different.
#Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def two_lowest(lst):
    # Sort the list in ascending order
    lst.sort()

    # Return the first two elements of the list
    return lst[:2]

# Define a list of numbers
lst = [4, 6, 2,4/2, 8, 5,0.5, 9, 1, 3, 7]

# Print the two lowest elements in the list
print(two_lowest(lst))