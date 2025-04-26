#Calculate factorial using loop
#Prompt the user to enter a number
number=int(input("Enter number:"))
#Set a condition using the while loop to ensure the user enters a number that can be calculated
while number<0:
    print("number can not be calculated")
#Initialize the product to 1
product = 1
#Use for loop to calculate the factorial then print the products
for a in range(1, number+1):
    product *=a
    print(product)