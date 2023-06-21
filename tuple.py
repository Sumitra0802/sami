#1
my_tuple = (10, 20, "a", "b", True)
print(my_tuple)

#2
print(my_tuple[3])

#3
tuple1 = (1,2,3)
tuple2 = ('x', 'y', 'z')
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)

#4
repeated_tuple = ((my_tuple)*3)
print(repeated_tuple)

#5
print(len(concatenated_tuple))

#6
sliced_tuple = my_tuple[2:5]
print(sliced_tuple) 

my_dist = {
    "Name" : "Samikshya",
    "Age" : 22,
    "Address" : {
        "Address1" : "Gorkha",
        "Zip" : {
            "Zip1" : 44800,
            "zip2" : 44600
        }
    }    
}
print(my_dist)

