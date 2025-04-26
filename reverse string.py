#Reverse a string
#create a string and name
string="city"
#Create an empty string that will be used to store the reversed string
reversed_string=''
#use for loop to loop through the string from the last to the first character
for m in range(len(string)-1, -1, -1):
    reversed_string +=string[m]
#print the final result
print(reversed_string)

