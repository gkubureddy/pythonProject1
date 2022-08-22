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
def Extract(new):
    return [list(set(item[0] for item in new)),list(set([item[-1]  for item in new]))]
new = a
print(Extract(new))




