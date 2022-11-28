def count_odd_even(n):
    odd  = 0
    even = 0
    while n > 0:
        current_digit = n % 10
        if current_digit % 2:
            odd = odd + 1
        else:
            even = even + 1
        n = n // 10
    return [odd, even]
test_n = 123455444412
test_result = count_odd_even(test_n)
print(test_result)

    #even_count, odd_count = 0, 0
    #for num in list:
        #if num % 2 == 0:
            #even_count += 1
        #else:
            #odd_count += 1



#list = [12,35,6]
#print (count_number)





