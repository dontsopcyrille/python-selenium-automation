def find_max_number_from(three_values):

        max =  three_values[0] #the [x]--> to specify that you have a list.
# of fait. reference a des nombres. ne reflechit pas met seulement
        for x in three_values:
            if x > max: #highest element x  in three values will be the
                #return result "max" since max=three_values
                #from every element in max=three_values(15,1,100),the highest
                #element (if  x > max) will be consider max max = x.
                max = x
        return max
three_values = [ -1, 1, 25/2]
print (find_max_number_from(three_values))


#logic 1:

#highest element "x"  in three values [ 15, 1, 100] will be the return
# result "max" since max=three_values. so, every element
# in max=three_values(15,1,100),the highest element (if  x > max)
# will be consider max cause "max = x"
#logic 2:most relevant logic
#max =  three_values[0]-----> now:
#si max est egale a three_value et que three_value a des
# element, three_values = [ 15, 1, 100]-->definit avec l'assertion
#"for x in three_values", alors if an element in three value is the
#highest "if x > max" donc that element x will be considered the
#highest.
# Key here :
# is the definition that "if x > max" signifie
#le plus grand element in our assertion --> qui veut dire que selon
#la logique python "if x > max" alors max= x  signifie le pus grand
# element in three_value qui est egale a max, definit plus tot avec
# max =  three_values[0] alors ce plus grand element
# sera le "return max" or le print de la function print (find_max_number_from(three_values))


