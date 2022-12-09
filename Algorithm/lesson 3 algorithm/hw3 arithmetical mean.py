def below_arithmetical_mean(lst):
    # Calculate the sum of the list
    total = sum(lst)

    # Calculate the number of elements in the list
    n = len(lst)

    # Calculate the arithmetical mean
    mean = total / n

    # Initialize the result list
    result = []

    # Iterate over the elements of the list
    for elem in lst:
        # Check if the element is below the arithmetical mean
        if elem < mean:
            # Add the element to the result list
            result.append(elem)

    # Return the result list
    return result
# Define a list of numbers
lst = [100,15,1000,765.100000]

# Print the elements below the arithmetical mean
print(below_arithmetical_mean(lst))