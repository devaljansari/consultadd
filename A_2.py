'''1. Write a program in Python to perform the following operation:   \
If a number is divisible by 3 it should print “Consultadd” as a string   \
If a number is divisible by 5 it should print “c” as a string   \
If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string.'''
n = int(input('Enter the value : '))
if n % 3 == 0:
    print('Consultadd')
elif n % 5 == 0:
    print('c')
elif n % 3 == 0 & n % 5 == 0:
    print("Consultadd Python Training")

'''2. Write a program in Python to perform the following operator based task: \
Ask user to choose the following option first: \
If User Enter 1 - Addition    \
If User Enter 2 - Subtraction    \
If User Enter 3 - Division     \
If USer Enter 4 - Multiplication     \
If User Enter 5 - Average     \
Ask user to enter the 2 numbers in a variable for first and second for \
the first 4 options mentioned above.\
Ask user to enter two more numbers as first and second for calculating \
the average as soon as user choose an option 5.\
At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”'''
print("Choose the operation from below")
print("1.Addition")
print("2.Subtraction")
print("3.Division")
print("4.Multiplication")
print("5.Average")

choice = int(input("Enter choice(1/2/3/4/5): "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    result = a + b
    print(result)
elif choice == 2:
    result = a - b
    print(result)
elif choice == 3:
    result = a / b
    print(result)
elif choice == 4:
    result = a * b
    print(result)
elif choice == 5:
    c = float(input("Enter first number: "))
    d = float(input("Enter second number: "))
    result = (c + d) /2
    print("Average of" , c, "and" ,d, "is :" , result )
if result < 0:
   print("Negative")
