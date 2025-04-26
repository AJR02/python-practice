#Check if a number is odd or even
#Come up with numbers that will be used
numbers=[21,28,35,32,49]
for number in numbers:
    #use % to check if the number is even or odd
    if (number%2==0):
    #use if loop to differenciate the even number from the odd number and print them
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")