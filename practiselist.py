my_list = ["mango","litchi", "tomato", "medicine"]
my_list.append("Carrot") #to add at last
my_list[3] = "Saag" #to replace item
my_list.insert(2,"Kakro") # to add in between
my_list.remove(my_list[0]) #to remove items
my_list.remove("litchi") #" " " "
forget = my_list.pop(2)
print(f"I forgot: {forget}")
print(f"I bring: {my_list}")

for x in range(len(my_list)):
    a = my_list[x]
    print(a)
