def HR_MT(x):
       return(x*60)
x = HR_MT(float(input("Enter hour:")))
print("Here is the desired minute:", x)

numbers = [3, 1, 4, 1, 5]
numbers.sort() 
print(numbers[2])

#Create a list called fruits with items: "apple", "banana", "cherry". 
# Add "orange" to the end, remove "banana", and 
# sort the list alphabetically. 
# Print the final list and its length.

fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("orange")
print("After adding:", fruits)
fruits.pop(1) # del fruits[1] or fruits.remove("banana")
print("After removing:", fruits)
fruits.sort()
print("Final list", fruits, len(fruits))

#Create a dictionary called student with keys: name, age, and grade. 
# Add a new key city with any value. 
# Update the grade to a new value. 
# Print all keys and the final dictionary.

student = {
    "name": "Alim",
    "age": "36",
    "grade": "A"
}
print(student)
student["city"] = "Dhaka"
print("After adding:", student)
student.update({"grade": "F"})
print("After updating:", student)
print("All keys:", student.keys())
print("Final dictionary:", student)


#Write a function calculate_total(price, quantity, discount=0) that calculates total cost. 
# The discount parameter should default to 0. 
# Return the final price after applying the discount percentage. 
# Test with: calculate_total(100, 2, 10) 
# (should return 180).

def calculate_total(price, quantity, discount=0):
    total_cost = price*quantity
    discount_percentage = total_cost * (discount/100)
    final_price = total_cost - discount_percentage
    return(final_price)
price=100
quantity=2
discount=10
print(calculate_total(price, quantity, discount))
