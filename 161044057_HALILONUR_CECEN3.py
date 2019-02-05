def digit_multiplier(number):
        result=1 # you should initiliaze the final result
        ##your code part
        list1=[]
        for i in str(number):
                if int(i)!=0 :
                        list1 = list1 +[i]
                        
        for x in list1 :
                result = result*int(x)
        return result
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert digit_multiplier(123405) == 120
    assert digit_multiplier(999) == 729
    assert digit_multiplier(1000) == 1
    assert digit_multiplier(1111) == 1
