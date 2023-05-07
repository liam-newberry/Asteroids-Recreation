list = [[50,40,30], [40,20,90],[10,20,30]]

a=[1,2,3]
b=a.copy()

a.pop(2)
print("!", b,a )

for i in list:
    if i[2] == 90:
        i.pop(2)
        i.insert(2, -40)
        print(list.index(i))
print(list)
