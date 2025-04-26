#sum of digits of a number
#Provide the number to be calculated
number=11726
#Initialize variable that will store the sum of the digits
total= 0
#use while loop until the number becomes 0
while (number>0):
#Rem to represent the last digit gotten
    rem=number%10
#Add the rem gotten to the total
    total=total+rem
#Remove last digit from number
    number=number//10
#print the result of total
print(total)