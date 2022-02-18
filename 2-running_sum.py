# Calculate a running sum

x = int(input("Write a number: \n"))
summ = 0

while x >= 0:
    summ += x
    print()
    print("The total is: ", summ)
    print()
    x = int(input("Write a number: \n"))
print("Negative numbers not accepted. Your sum total is: ", summ)


    # Output
Write a number: 
2

The total is:  2

Write a number: 
3

The total is:  5

Write a number: 
3

The total is:  8

Write a number: 
-1
Negative numbers not accepted. Your sum total is:  8
