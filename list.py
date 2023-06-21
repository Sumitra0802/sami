#1
numbers = [1,3,5,7,9]
print(numbers)

#2
print(numbers[1])

#3
numbers[2] = 10
print(numbers)

#4
numbers.append(12)
print(numbers)

#5
numbers.remove(numbers[2])
print(numbers)

#6
sliced_list = numbers[1:5]
print(sliced_list)

#7
combined_list = numbers + sliced_list
print(combined_list)

#8
print(8 in combined_list)

#9
combined_list.sort()
print(combined_list)


combined_list = list(dict.fromkeys(combined_list)) #to remove repetative items from the list.
print(combined_list)

