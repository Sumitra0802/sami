my_tuple = (99,8,1,2,1,3,4,5)
my_tuple2 = (99,1,2,3,4,5)
print(my_tuple+my_tuple2)
new_tuple = sorted(my_tuple,reverse=True)
print(type(new_tuple))
print(type(tuple(new_tuple)))
print(min(new_tuple))
print(max(new_tuple))
