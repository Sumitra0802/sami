#WAP to show the multipication table of 1st 20 prime numbers.
'''def prime_num(number):
    if number<2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number %i==0:
            return False
        return True
count=0
number=1
prime_list=[]
while count<20:
    if prime_num(number):
        prime_list.append(number)
        count=count+1
    number=number+1
print(prime_list)

def mul_table(a):
    for i in range(1,11):
        print(f"{a}*{i}={a*i}")
    print("............")

for i in range(0,20):
    mul_table(prime_list[i])
'''    
    
#WAP to find simple interest.
'''
p=int(input("Enter the principal:"))
t=int(input("Enter the time:"))
r=float(input("Enter the rate:"))
Sim_interest=(p*t*r)/100
print("The simple interest is:",Sim_interest)

'''

#WAP to find a perimeter of a rectangular ground.

'''
l= int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
perimeter = (2*(l+b))
print("The perimeter of a rectangular ground is:", perimeter)

'''

#WAP to find volume of irregular body.
#wap to calculate volume of a cube.
#WAP to find square root of a number.
#WAP to find error percetage.
#take a string as a input from a user and check whether a string is Rishab Karki or not.


#WAP to find area of a circle with radius7.5,8.97,20,39,100,129,139,600,1000,5.6,8.9,12.7,11.2.
# list=[]
# pie=3.14
# radius=[7.5,8.97,20,39,100,129,139,600,1000,5.6,8.9,12.7,11.2]
# print(radius)
# def area(radius):
#     for i in radius:
#         area=pie*(i)**2
#         print(area)
# area(radius)


#show index
# fruits=["Apple","Banana","Mango"]
# for index,value in enumerate(fruits):
#     #print(index+1,value) 
#     print(index,value) 


#copy, make changes and display.
# import copy
# list_a=[1,2,3]
# list_b=list_a
# list_b=copy.deepcopy(list_a)
# list_b[2]=("Samikshya")
# print(list_a)
# print(list_b) 

#print 3/3 matrix.
# a=[[1,1,1],[2,2,2],[3,3,3]]
# print(a)
# for i in range(0,3):
#     for j in range(0,3):
#         a[i][j]=i+1+a[i][j]
# print(a)



# tuple1= (1,2,3)
# for i in tuple1:
#     print(i)
    
    
    

        
            