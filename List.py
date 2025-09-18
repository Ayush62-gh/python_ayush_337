list1 = ["rohan",3]
list1 = ["rohan",1,3,"rohan","apple","apple"]
print(len(list1))

#constructor
list2=list(("rohan",1,3,"rohan","apple","apple"))

#access item in list
print(list1[1])

#negative indexing
print(list1[-1])

#range of index
print(list1[1:4])

#range of negative index
print(list1[-4:-1])

#check if item exists
if "rohan" in list1:
    print("yes")

#change list item
list1[0]="ram"
print(list1)

#change range of list
list1[1:3]=[5,6]
print(list1)

#insert item at specific index
list1.insert(2,"banana")
print(list1)

#append item at end
list1.append("orange")
print(list1)

#extend list
list1.extend(["mango","grape"])
print(list1)

#remove item
list1.remove("apple")
print(list1)

#remove last item
list1.pop()
print(list1)

#clear elements
#list1.clear()
#print(list1)
#deletes list and elements
#del list1
#print(list1)

#loop
# i=0
# while i<len(list1):
#    print(list1)
#    i=i+1

#convert letters into uppercase
fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[x.upper() for x in fruits]
print(newlist)

#convert first letter into uppercase
fruits1=["apple","banana","cherry","kiwi","mango"]
newlist1=[x.capitalize() for x in fruits1]
print(newlist1)

#sorting(in ascending order)
list3=[100,50,65,82,23]
list3.sort()
print(list3)

#sorting(in descending order)
list3.sort(reverse=True)
print(list3)
list3.reverse()
print(list3)

#case insensitive sorting
thislist=["Apple","BAnana","cherry"]
thislist.sort(key=str.lower)
print(thislist)

#reverse order
thislist=["Apple","Banana","cherry"]
thislist.reverse()
print(thislist)

#copy list
list4=list3.copy()
print(list4)

#slice operator
list5=list3[:]
print(list5)

#join two lists
list6=[1,2,3,4,5]
list7=["a","b","c","d","e"]
list8=list6+list7
print(list8)

#append method
#for x in list7:
#    list6.append(x)
#print(list6)

#extend method
list6.extend(list7)
print(list6)