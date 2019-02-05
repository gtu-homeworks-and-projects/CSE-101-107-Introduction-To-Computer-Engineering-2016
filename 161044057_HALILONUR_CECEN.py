x=int(input("First Integer: "))
y=int(input("Second Integer: "))

xdigitnmbr=int(len(str(x))) 
ydigitnmbr=int(len(str(y))) 
loopcounter=min(xdigitnmbr,ydigitnmbr) 
counter=0 

while (loopcounter>0):
    if (x%10)==(y%10):
        counter=counter+1
    else :
        break
    loopcounter=loopcounter-1
    x=int(x/10)
    y=int(y/10)
print("The number of matching digits starting from right: ",counter )
