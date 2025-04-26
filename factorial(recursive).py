#Calculate factorial of a number through recursive method
def factorial(number):
#use if loop to ensure that the integer calculated is >=0
    if number == 0 :
        return 1
#create a recursive step
    return number * factorial(number-1)
#create number that contains a integer that will be calculated using factorial
number=[7]
for a in number:
#print the result
    print(factorial(a))