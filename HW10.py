class SortedList:
    def __init__(self):
        self.theList=[1,2,3,4,5,6,8,11,14,15,19]
        self.tempList=self.theList
        self.found=1
        self.not_found=0
    def add(self, number):
        for n in range(len(self.theList)):
            if self.theList[n]>=number:
                self.theList.insert(n,number)
                print(number,"Added to List")
                break

    def remove(self, number):
        if self.binarySearch(number)==True:
        	self.theList.remove(number)
        	print(number,"Removed from the List")
        else:
        	print("Can't remove",number)


    def binarySearch(self, number):
        high=len(self.tempList)
        index=int(len(self.tempList)/2)
        if high==0:
            print("The List is Empty")
        else:
        	if self.tempList[index]==number:
        		print(number,"Found in the List")
        		self.tempList=self.theList
        		return True
        	elif high==1 and self.tempList[index]!=number:
        		print(number,"Not Found in the List")
        		self.tempList=self.theList
        		return False
        	elif self.tempList[index]<=number:
        		self.tempList=self.tempList[index:]
        		return self.binarySearch(number)
        	elif self.tempList[index]>=number:
        		self.tempList=self.tempList[:index]
        		return self.binarySearch(number)

    def printList(self):
    	print(self.theList)
        	


sorted = SortedList()

sorted.add(-1)
sorted.add(16)
sorted.add(17)
sorted.add(18)
sorted.add(50)

sorted.remove(19)
sorted.remove(55)

for x in range(20):
	sorted.binarySearch(x)

sorted.printList()