#task
#our code generates random three-digit number and has to sum up
#all its digits
def sum_of_three(n): #257
    result = 0
    while n !=0: # result = 14# ;n = 0
        result = result + (n % 10)
        #second round
        n = n // 10 # 2/ 10 = 0
    return result
number = 12345 #expect to see 14
result =  sum_of_three(number)
print(result)
print(15 / 2)# a test

#Sum of three digits second way and easiest way
def sum_of_three_numbers(x, y, z):
    sum = x + y + z
    if x == y == z:
        sum == sum * 3  # this works no matter which number in
        # puted,if 5 was the number,result would have been the same
    return sum


print(sum_of_three_numbers(1, 1, 1))
print(sum_of_three_numbers(1, 2, 3))
#time complexity here is O(n)


# different type Algorithm logic exercises
#==============================================================
#==============================================================

#1-find the max number in a list
def find_max_number_from(three_values):
    max = three_values[0]  # the [x]--> to specify that you have a list.
    # of fait. reference a des nombres. ne reflechit pas met seulement
    for x in three_values:
        if x > max:  # highest element x  in three values will be the
            # return result "max" since max=three_values
            # from every element in max=three_values(15,1,100),the highest
            # element (if  x > max) will be consider max max = x.
            max = x
    return max


three_values = [-1, 1, 25 / 2]
print(find_max_number_from(three_values))


#==============================================================
#==============================================================
#2-differrent types  algoriyhms solution
#1- some of 3 digits
def sum_of_three(n): #257
    result = 0
    while n !=0: # result = 14# ;n = 0
        result = result + (n % 10)
        #second round
        n = n // 10 # 2/ 10 = 0
    return result
number = 12345 #expect to see 14
result =  sum_of_three(number)
print(result)
print(15 / 2)# a test
#=============================================================
#==============================================================def is_leap_year(year):
#3-factorial
def factorial(n):
    result = 1 #definit que result(1) is 1(formule factorial)
    for i  in range(1, n + 1): # condition(formule factorial)
        print(i) # not needed but just to see range of number
        result = result * i #(same as result *= i)-this is
    return result  # return is used to say we are stopping the
# the execution of a function and we are returning a value
number = 5  # define number to be factorial et in other word,
# 5 is range 1 to 5 according to formula range(1, n + 1)
result = factorial(number)  # meaning print la function
#def factorial given that number(not n ) is 5
print(result)


#4-leap year
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'{year} is a leap year')
            else:
                 print(f'{year} is not  a leap year')
        else:
            print(f'{year} is a leap year')
    else:
        print(f'{year} is not  a leap year')
#we have 4 prints for our 4 years
is_leap_year(2007)
is_leap_year(1900)
is_leap_year(2012)
is_leap_year(2000)
#=============================================================
#==============================================================d

#task : run the 3 bellow funtion consecutively
#-first function
#function get two numbers that will represent number of trophees
#of  the two best soccer players alive.one player is assigned
#an amount  of trophees and the other player is assigned to
# another amount of trophees

#-second function
#function get two numbers that will represent speed of 2 electric
#cars.One number is assigned to one car The other number is
# assigned to another car.#The task is to invert the
# variables,so that the first car contains the speed of the
#second car,while the second car is  the speed of the
# first car

#-third function
#function get two numbers. One number is assigned to a variable
#The other number is assigned to another variable.
#The task is to invert the variables,so that the first variable contains the
#second number,while the first number is in the second variable.
# ============================================================
#=============================================================
# first function solution 1
def best_player_trophees(messi, ronaldo): #messi=7 , ronaldo=5
    print(f'messi = {messi} , ronaldo = {ronaldo}')

def best_player_trophees(messi, ronaldo):  # messi=7 , ronaldo=5

            print(f'messi = {messi} , ronaldo = {ronaldo}')
            messi , ronaldo =  ronaldo , messi
            print(f'messi = {messi} , ronaldo = {ronaldo}')
best_player_trophees(7, 5)


def fastest_car_speed(tesla, lucid): #tesla=1000 , lucid=100
    print(f'tesla = {tesla} , lucid = {lucid}')
    change=tesla
    tesla = lucid
    lucid = change
    print(f'tesla = {tesla} , lucid = {lucid}')
fastest_car_speed(1000, 100)

# second  function solution 2
def fastest_car_speed(tesla, lucid): #tesla=1000 , lucid=100
    #this swapping method is the best from the 3
    print(f'tesla = {tesla} , lucid = {lucid}')#first print
    tesla, lucid = lucid, tesla#swapping occur with this
    print(f'tesla = {tesla} , lucid = {lucid}')#second print
fastest_car_speed(1000, 100)

# second  function solution 3
def fastest_car_speed(tesla, lucid): #tesla=1000 , lucid=100
    print(f'tesla = {tesla} , lucid = {lucid}')
    tesla = tesla + lucid # 1000 + 100 = 1100 #--> nouvelle
    lucid = tesla - lucid # 1100 - 100 = 1000
    tesla = tesla - lucid # 1100 - 100 = 100
    print(f'tesla = {tesla} , lucid = {lucid}')
fastest_car_speed(1000, 100)

#third function solution 1
def swap_two_variables(a, b): #a =2, b =4
    print(f'a = {a}, b = {b}')

    change = a  # 2 -->what allow the swapping
    a = b  # 4    -->what allow the swapping
    b = change  # -->what allow the swapping

    print(f'a = {a}, b = {b}')
swap_two_variables(2 , 4) #-->what defines numbers a and b

def swap_two_variables(a, b):
    print(f'a = {a}, b = {b}')#first print
    a, b = b, a#swappi  ng occur with this
    print(f'a = {a} , b = {b}')#second print
fastest_car_speed(1000, 100)
