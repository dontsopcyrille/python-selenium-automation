#Write a program that prints the numbers from 1 to  100,but for multiples
 #of three print "Fizz" instead of the number and the multiples of
 #five print  "Buzz".
#For numbers whhich are multiples of both three and five print "FizzBuzz"
#example:
#1
#2
#Fizz
#4
#...
#8
#Fizz
#10
#...
#14
#FizzBuzz

def fizzbuzz():
    for i in range(1,101): #meaning for each number in range or
#meaning on definit que tout nombre
#dans le range  1-101 est considerer i and print will return
#any number that you put in the range and it does not have to
# be part of range
        print(10000000)
fizzbuzz()
#==============================================================
#==============================================================
#original code
 #meaning on definit que tout nombre
# dans le range  1 -101 est considerer i et dans notre original
#code vu que i esr considerer le range,les nombre from 1 to 101
#consecutive will be printed
def fizzbuzz():
    for i in range(1,101):
     if i % 3 == 0 and i % 5 == 0:# %=division,i % 3 == 0-->
    #meaning a number divided by 3 without a remainder-->
    # == 0  means for un nomber i % 3,we dont want a remainder
    #basically when there is no remainder it means that we have
    # a muliple. 10 % 3==3 and the remainder is 1

            print("FizzBuzz")  # multiple of 3 and 5 print FizzBuzz
     elif i % 3 == 0:  # multiple of 3 print Fizz

            print("Fizz")
     elif i % 5 == 0: # multiple of 5 print Fizz
            print("Buzz")
     #elif is used when you have multiple conditions and if
     #the above "if" or "elif" statement are false

     else:#else is when all above condition(if and elif) are false

            print(i)
fizzbuzz()
3#O=(n1) --> big O for this function is also O(n) or linear time
#becbeause each line is checked or each line is executed
# consecutively or time complexity is linear