i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)

fruits = ["apple", "banana","cherry"]
for x in fruits:
    print(x)
    if x=="banana":
        break

#nested loop
a=["A","B","C"]
fruits = ["apple", "banana","cherry"]
for x in a:
    for y in fruits:
        print(x,y)