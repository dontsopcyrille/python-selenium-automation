# \"\" inside a function to quote  sentences or worlds
# ---->     \"xxxxx\"
#basically,a quote in a sting.--> a string is already quoted

test_string = "this is my \"string\""
print(test_string)
#=============================================================
#==============================================================
# the  'in' syntax
#used to cetermine if a letter or a substring ecists in a
#string(word or collection or words in quote to define sth).
#it returns True if a match is found otherwhise false is return

#here result will be empty in prompt since () is empty
test_string = "this is my  string"
if "i" in test_string:
    print()
else:
    print()





#=============================================================
#=============================================================
test_string = "this is my  string"
if "i" in test_string:
    print("i  is in the  test_string")
else:
    print("i  is  not in the  test_string")
#example2 for understanding
test_string = "this is my  string"
if "v" in test_string:
    print("x  is fuck test_string")
else:
    print("y  is  anango in the  test_string")
#==========================================================
#==========================================================
# example3 for understanding
test_string = "this is my  string"
if "v" in test_string:
    print("v  is fuck test_string")
else:
    print("now you understood the logic")