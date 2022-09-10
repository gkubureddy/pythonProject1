#1.Implement palindrome using iterator(for loop) and generator mechanism

def palin_generator():
    """Generates palindromic numbers."""

    palindromes=[]
    for count in range(100):
        n = str(count)
        if n == n[::-1]:
            palindromes.append(n)
    yield palindromes

obj = palin_generator()
#print(next(obj))
for i in palin_generator():
    print(i)

#2.Sum of 2 digits into output
n1 = 1234     # int(input("Enter number1 :" ))
n2 = 9999     # int(input("Enter number2 :" ))
print('orginal_numbers:' + str(n1))
print('orginal_numbers:' + str(n2))
temp = [n1[x]+n2[x]for x in range(len(n1))]
print("sum of two digits is:" + str(temp))

#5. t1 = (1, 2, 3, "a", "c")
#    t2 = ("b", "d", 9, 8, 7)
#    Output: (10,10,10,"ab","cd")
def join_list(t1,t2):
    temp = []
    for i in t1:
        for j in range(len(t2)):
            if(type(i) is type(t2[j])):
                temp.append(i+t2[j])
                t2.remove(t2[j])
                break
    return temp

t1 = [1, 2, 3, "a", "c"]
t2 = ["b", "d", 9, 8, 7]
print(join_list(t1,t2))
#6 Write a Python program to remove leading zeros from an IP address.
			  inp = "216.08.094.196"
			  # o/p =  216.8.94.196

def ipadd(str1):
    str2 = ""
    for i in str1:
        if i != "0":
            str2 = str2+i
    return str2

print(ipadd(input("Enter the IP address: ")))

#4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
   #findout elements duplicate count output in  dict format
some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
container={x:some_list.count(x) for x in some_list}
ties = dict()
for key,value in container.items():
    if value>1:
        ties[key]=value

print(ties)

# 7. l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
#    #output= [1,2,3,4,5,6,7,8,9,10]
list1 = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
output = []
def removeNest(list1):
    for i in list1:
        if type(i) == list:
            removeNest(i)
        else:
            output.append(i)
removeNest(list1)
print("the list after removing nested:",output)


