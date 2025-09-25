d={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "mode":"F-150"
}
print(d)
print(len(d))
print(type(d))
d1=dict(brand="Ford",model="Mustang",year=1964)
print(d1)
#pop
d.pop("model")
print(d)
#popitem
d.popitem()
print(d)
#del
del d["year"]
print(d)
#type
print(type(d))
#for loop
for x in d:
    print(x)
    print(type(x))

#copy(copies whole dictionary into a new dictionary)
d2=d1.copy()
print(d2)
print(type(d2))

#clear
d2.clear()
print(d2)
print(type(d2))
