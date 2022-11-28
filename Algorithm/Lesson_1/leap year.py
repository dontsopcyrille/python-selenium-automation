#task
# year or not
#1024-True/false
#a leap year is exactly divisible by 4 except for  century years
#(years ending with 00)
#The century year is a leap year only if it is perfectly
# divisible 400
#2007 is not a lap year
#1900 is not a leap year
#2012 is a leap year
#2000 is a leap year
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
# big O is  0(1)  cause the  time complexity is constant time
# cause we always take same amount of accuration to calculate
#if it is a leap year or no
