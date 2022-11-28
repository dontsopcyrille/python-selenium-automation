#task
#Compute the sum of digits in all numbers from 1 to n. When a
#funtion gets a number n, find the sum of digits in all numbers
#from 1 to n.
#Example:n=5 Result=1+2+3+4+5=15
def factorial(n):
    result = 0
    for i  in range(1, n + 1 ):
        print(i)  # not needed but just to see range of number
        #and last number is result
        result = result + i

    return result

number = 3
result = factorial(number)
print(result)
