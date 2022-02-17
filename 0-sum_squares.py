user_input = input('Please write 5 numbers separated by spaces. Do not use commas: \n')


user_list = user_input.split()
print(user_list)
print()

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

print(user_list)
print()

list_sqd = []
for numbers in user_list:
    list_sqd.append(numbers**2)

print(list_sqd)
print(sum(list_sqd))


# Output 

Please write 5 numbers separated by spaces. Do not use commas:
1 2 3 4 5 
['1', '2', '3', '4', '5']

[1, 2, 3, 4, 5]

[1, 4, 9, 16, 25]
55
