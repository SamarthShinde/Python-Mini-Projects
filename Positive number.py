n=int(input("enter a number in list : "))
list=[]
for i in range(n):
    a=int(input("enter a number :"))
    list.append(a)
print("the user define list is :")
print(list)
pos_list=[]
for n in list:
    if n > 0:
        pos_list.append(n)
print("\n")
print("the list of just positive number is :")
print(pos_list)


