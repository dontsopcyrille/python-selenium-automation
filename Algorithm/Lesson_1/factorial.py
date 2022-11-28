#task
#When Function gets a number , its factorial is displayed.
#nb: factorial is only for natural number like 1,2,3,-5 etc and
# is not for rational number like 1.5

def factorial(n):
    result = 1 #definit que result(1) is 1(formule factorial)
    for i  in range(1, n + 1): # condition(formule factorial)
#et nous donne le range du nombre qui es  de "1" a n+1 qui veut
#dire range indeterminer et par consequent n+1 definit donc la
# fin du range definit par le numbre inputed a "number"
        print(i) # not needed but just to see range of number
        result = result * i #(same as result *= i)-this is
# actually the formula and definition of 2nd form of result(2)
# if result=1 , 1 * i  is 1*(1, n + 1)-> car result = result * i
#so given that we have a number defined 5-->, result will be
#1*1 * 1*2 * 1*3 * 1*4 * 1*5 car number 5 give range (1,2,3,4,5)
#according to formula  i  in range(1, n + 1),so will result *= i
#will multiply every number of the range
    return result  # return is used to say we are stopping the
# the execution of a function and we are returning a value

#here are the characteristic of the function
number = 5  # define number to be factorial et in other word,
# 5 is range 1 to 5 according to formula range(1, n + 1)
result = factorial(number)  # meaning print la function
#def factorial given that number(not n ) is 5
print(result)

#time complexity here is also O(n) because we will execute
#result*=  i # (same as result = result * i) as many time as
#we have a number. For instance 25! will execute that line
#25 time or 10!=line will be executed 10 times

#comparison in terms for 3 different functions:factorial,
#swap algorithm or change consecutive defined value with
# each other variabe , and fizz and buzz  or replace
# a range of  number  by a term