'''1. Create three variables in a single line and assign different values to them and make sure \n
their data types are invited different. Like one is int, another one is float and last one is string.'''

a , b, c = 1, 2.4, 'Deval'
print(a)
print(b)
print(c)

'2. Create a variable of value type complex and swap it with another \
variable whose value is an integer.'
a = 2 + 3j
b = 4
a, b = b, a
print(a)
print(b)

"3. Swap two numbers using third variable as result name and do the same task \
without using any third variable."
a = 7
b = 9

result = a
a = b
b = result
print(a)
print (b)

a = 2
b = 4
a, b = b, a
print(a)
print(b)

"""4. Write a program to print the value given by the user by using both Python 2.x 
and Python 3.x Version.

s = eval(raw_input('Enter value using python 2.x :'))
print(s)

s_1 = eval(input('Enter value using python 3.x :'))
print(s_1)"""

'5. Write a program to complete the task given below:\
Ask user to enter any 2 numbers in between 1-10 and add both of them to another variable  call z.\
Use z for adding 30 into it and print the final result by using variable result.'

x = int(input("Enter the First Value between 1 - 10  : "))
y = int(input("Enter the Second Value between 1 - 10  : "))
z = x + y
result = z + 30
print(result)

'6. Write a program to check the data type of the entered values. \
HINT: Printed output should say -  The input value data type is : int/float/string/etc'

x = input("Enter the value : ")
print('The input value data type is : ', type(x))

"""7. Create Variable using CamelCase, LadderCase and UPPERCASE."""
'a = FedEx'
'b = FEDEX'
'c = Fedex'

"8. If one data type value is assigned to ‘a’ variable and then a different \
data type value is assigned to ‘a’ again. Will it change the value. If Yes then Why?"

'Yes the value will be changed because it will be'
n = 2
n = 3
print(n)

