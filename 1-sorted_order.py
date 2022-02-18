# Reads in 3 numbers
# and writes them all
# in sorted order...


num1 = int(input(" Give me a number: \n"))
num2 = int(input(" Give me another number: \n"))
num3 = int(input(" Give me one last number: \n"))

if num1 < num2 < num3:
    print(num1, num2, num3)

elif num1 < num3 < num2:
    print(num1, num3, num2)

elif num2 < num1 < num3:
    print(num2, num1, num3)

elif num2 < num3 < num1:
    print(num2, num3, num1)

elif num3 < num1 < num2:
    print(num3, num1, num2)

elif num3 < num2 < num1:
    print(num3, num2, num1)
    

# Output
 
 Give me a number: 
55

 Give me another number: 
10

 Give me one last number: 
25

10 25 55
