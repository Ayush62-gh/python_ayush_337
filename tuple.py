tuple1 = ("apple","banana","cherry")
print(tuple1)
print(len(tuple1))
tuple2 = (1,5,7,9,3)
tuple3 = (True,False,False)

#constructor
T = tuple(("apple","banana","cherry","kiwi"))
print(T)
print(T[-2])
#range of indexes
print(T[1:3])
if "apple" in T:
    print("yes, 'apple' is in the tuple")
#cannot change values in tuple
#T[0]="kiwi" #gives error because tuples are immutable
#but we can convert tuple to list and change it
L =list(T)
L[0]="kiwi"
T=tuple(L)
print(T)

#add items
T1 = ("apple","banana","cherry")
T2 = ("orange",)
T3 = T1 + T2  
print(T3)

#remove items
#tuples are immutable so we cannot remove items but we can convert it to list and remove
L = list(T3)
L.remove("apple")
T3 = tuple(L)
print(T3)

#unpacking a tuple
fruits = ("apple","banana","cherry","orange","kiwi","mango")
(green,*yellow,red) = fruits
print(green)
print(yellow)  
print(red)

#loop through a tuple
for x in T3:
    print(x)