#Program to show different set operations

list1 = []
list2 = []

n = int(input("No. of elements for set 1: "))
m = int(input("No. of elements for set 2: "))

for i in range (0,n):
    a = int(input("Enter element for set 1: "))
    list1.append(a)
for j in range (0,m):
    b = int(input("Enter element for set 2: "))
    list2.append(b)

s = set(list1)
t = set(list2)
print("---------------------------------------------")
print("Union of the sets is : ", s | t)
print("Intersection of the sets is : ", s & t)
print("Difference of the sets is : ", s - t)
print("Symmetric difference of the sets is : ", s ^ t)
print("---------------------------------------------")
