#Program to print Fibonacci sequence

terms = int(input("Enter the number of terms you want in the sequence: "))

a, b = 0, 1
count = 0
if terms == 1:
    print("Fibonacci sequence: ", a)

elif terms <=0:
    print("Entry invalid. Please enter another input")

else:
    print("Fibonacci sequence: ")
    while count < terms:
        print(a)
        c = a + b
        a = b
        b = c
        count += 1


    
