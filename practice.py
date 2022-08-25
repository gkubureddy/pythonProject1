a = [['A','Laptop'],['A','Laptop'],['A','Mouse'],['B','Laptop'],['A','Headset'],['B','Headset']]
count_A = 0
count_B = 0
temp = []
for i in a:
    if i[0] == 'A':
        count_A += 1
    if i[0] == 'B':
        count_B += 1
temp.append([['A',count_A],['B',count_B]])
print(temp)
print([['A', 'Laptop',a.count(['A','Laptop'])],['A','Mouse',a.count(['A','Mouse'])],
      ['B','Laptop',a.count(['B','Laptop'])],['A','Headset',a.count(['A','Headset'])],
      ['B','Headset',a.count(['B','Headset'])]])

# tuple with different data types

a_1 = (4,'shruthi', 2.6)
b= list(a_1)
print(b)

#copy method

b_2 = ["apple","bat"]
c = list( b_2)
print(c)

#join method

a = "Hello"

c = ' '.join(i for i in a)
print(c)

#replace method
a = "Vn2solutions"
print("*replace method*")
b = a.replace('Vn2','Vn2  ')
print(b)





