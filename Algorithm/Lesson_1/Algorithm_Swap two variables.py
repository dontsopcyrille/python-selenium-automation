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
#O=(n1) --> big O for this function is (n1) or consecutive time
#because each line is checked or each line is executed consecutively

#first function solution 2

#second function solution 1
def fastest_car_speed(tesla, lucid): #tesla=1000 , lucid=100
    print(f'tesla = {tesla} , lucid = {lucid}')
    change=tesla
    tesla = lucid
    lucid = change
    print(f'tesla = {tesla} , lucid = {lucid}')
fastest_car_speed(1000, 100)
#O=(n1) --> big O for this function is (n1) or contant time
#because each line is checked or each line is executed consecutiv

# second  function solution 2
def fastest_car_speed(tesla, lucid): #tesla=1000 , lucid=100
    #this swapping method is the best from the 3
    print(f'tesla = {tesla} , lucid = {lucid}')
    tesla, lucid = lucid, tesla
    print(f'tesla = {tesla} , lucid = {lucid}')
fastest_car_speed(1000, 100)
# second  function solution is much more faster cause we cut
#3 line"change=tesla,tesla = lucid,lucid = change)
# to replace by one line("tesla, lucid = lucid, tesla")
#O=(n1) or O(n)1--> big O for this function is also (n1) or contant time
#becbeause each line is checked or each line is executed
# consecutively even though we have less time

# second  function solution 3
def fastest_car_speed(tesla, lucid): #tesla=1000 , lucid=100
    print(f'tesla = {tesla} , lucid = {lucid}')
    tesla = tesla + lucid # 1000 + 100 = 1100 #--> nouvelle
    #valeur integrated qui n'appartient a aucune definition
    #met qui nous permet d'aboutir a un resultat rechercher
    #nous permettant de definir une base(parceque tout concept
    #theorique en science nest  que question de base
    # tesla = tesla + lucid-->si on considere que
    # tesla=tesla+lucid ayant definit des variable pour tesla
    #et lucid alors on peut aboutir au resultat qu'on souhaite
    #a savoir inverser les roles pour que tesla=100 et
    #lucid=1000
    #en conclusion,algorithm cest chercher toutes les definition
    #possible qui permettent d'aboutir au resultat souhaiter
    lucid = tesla - lucid # 1100 - 100 = 1000
    tesla = tesla - lucid # 1100 - 100 = 100
    print(f'tesla = {tesla} , lucid = {lucid}')
fastest_car_speed(1000, 100)
#O=(n1) --> big O for this function is (n1) or contant time
#because each line is checked or each line is executed
# consecutively even though we have less line





#third function solution 1
def swap_two_variables(a, b): #a =2, b =4
    print(f'a = {a}, b = {b}')
    #nb:swap can be any word or letter and we just define that word
    #with a variable or a number
     #like the bellow replacement will also work:
    # change = b  # 2 -->what allow the swapping
    #a = b  # 4    -->what allow the swapping
    #b = 2  # -->what allow the swapping
      # 2 -->what allow the swapping
    change = a  # 2 -->what allow the swapping
    a = b  # 4    -->what allow the swapping
    b = change  # -->what allow the swapping
    #we got to find a synonym for one of the character
    #otherwise function will be mixed up
    # and if you put swap =b like with a,the result

#would have been a =4, b=4
    print(f'a = {a}, b = {b}')
swap_two_variables(2 , 4) #-->what defines numbers a and b
#and if we remove what allow the swapping we will only get
#same result for the two prints that we ran
#a=2, b=4
#a=2,b=4
 #this is another function, and that
#will give our expected swapping result in console and that
#is why its indent is close to the margin,if we were to write
#note there like slighlty indentented,it would have been
#considered continuation of the first function def.
#element or line of code of same function should have same
#indent exect for the first line of new function that is close
#to margin
#O=(n1) --> big O for this function is (n1) or consecutive time
#because each line is checked or each line is executed consecutiv

#third function solution 2

