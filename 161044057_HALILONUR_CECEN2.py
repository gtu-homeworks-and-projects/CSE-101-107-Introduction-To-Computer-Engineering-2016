var1 = 175 #Assigning variable1.
var2 = 125 #Assigning variable2.
print('First Variable =' , var1 , '\nSecond Variable =' , var2 , sep=' ') #Printing variables individually.
#Switching variables using temporary variable.
print('\n -Variables swapped. \n')
tmp = var1 #Assigning variable1 to temporary variable.
var1 = var2 #Swapping variable1 with variable2.
var2 = tmp #Swapping variable2 with variable1 from temporary value.
#
print('First Variable =' , var1 , '\nSecond Variable =' , var2 , sep=' ')#Printing variables in the same order.



