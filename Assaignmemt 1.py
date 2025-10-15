#Problem: 01
#Write a Python program that takes a number as input and checks whether it is even or odd.
#solve
Number_input = int(input("Please input number:"))
if  Number_input % 2 != 0:
    print ("The number is odd")
else:
    print("The number is even")


#Problem: 02
#Write a program that takes two numbers and an operator (+, -, *, /) and performs the calculation.
#solve
num1 = float(input("Enter your value:"))
operator = input("Enter Operator (+, -, *, /): ")
num2 = float(input("Enter your value:"))
if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("Error detected")


#Problem: 03
#Write a program using a for loop that calculates the sum of even numbers between 1 and 100.
#solve
even_sum = 0
for num in range(1,101):
    if num % 2 == 0:
        even_sum += num
print("sum of even numbers:" , even_sum)