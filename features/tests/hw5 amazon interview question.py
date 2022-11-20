
#Create a function that will take a string as an input
#and return the 1st unique letter(element) of a string.
# example "google" => l -->cause l is first(not second or third)
#so the first character or input(letter number etc..) will
#be used to represent the string but has to be unique,
#meaning not  counted more than one time in the word
#“Amazon” => “m”
#If there are no unique letters, return an empty string: “xoxoxo” => “”.
#How would you test it? How would you handle edge cases?-->
#answer: we can test by using our terminal and print worlds
#print(unique('Google'))
#we also define case sensitive.So we can test by testing
#world starting with capital and lower case
#print(unique('Google'))
#print(unique('google'))







#bellow is function for unique element."l" does not mean
#is the letter l,but means it is an element
def unique(string: str):
     # Google => google
     string = string.lower()  # google

     for l in string:  # O(n)
#O(n) is linear time complexity,means every item in a list
#has to be loot at to acomplish task
         if string.count(l) == 1:  # O(n)
            return l
# => O(n^2)

#bellow is function that count number of element in a string and
#put thmem in { }
#without this function,when match is not found a "none" will
#be returned instead of an empty space in the result in terminal

def unique(string1: str): #any name in place of sting1 can be given
    string1 = string1.lower()  # google
#bellow is creation of a dictionary as reference with
#loop { }
#d=dictionary or the worlds that we are printing
    #here we are defining our dictionary
    d = {}
    for letter in string1:  # O(n)
    # we have 2 "for" and 2 "return"(characteristics of function)
        if letter not in d:
            d[letter] = 1  # => d = {'g': 2} for google(2 "g")
        else:
            d[letter] += 1 #count increase when element found
            #more than one. so 3 same element will give count 3
    print(d)

    for k, v in d.items():  # O(n)
#k=key or elememt , v=value or count , d.items=dictionary.items
#meaning the fist value in the string that has a count
#of 1 element, that elememt "key" will be returned (printed)
#translation:for an element if  count=1 return that element or
#the first element that has count of 1 will have its element printed
        if v == 1:
            return k

    return ''
    #return and empty string if  v # 1:
              #meanig if v is empty ore is more than 1,
#the print value will be an empty sting or space " "(space)
#will be empty without the commas
#could have also been rerun 'false"
# => O(n)





print(unique(',..?"+=+?'))
print(unique('d'))
print(unique('2345'))
print(unique('@&shgdfhg&*(hgshg'))
print(unique('Googllee'))
print(unique('Google'))
print(unique('google'))
print(unique('padlle'))
print(unique('Amazon'))
print(unique('google'))
print(unique('xoxo'))
print(unique(''))
print(unique('@&shgdfhg&*(hgshg'))
print(unique('k'))


