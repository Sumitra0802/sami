def adding (a,b,c,d):
    print(a,b,c,d)
adding(5,7,9,13)

def adding (a):
    print("Hello inside function with arguement",a)
val=adding(5)
print(val)

val=5
a=7
b=10
c=5
d=8
def adding():
    sum=5+9
    test=val
    test=test+4
    print(sum,a+b)
    multiply=5*9
    print(multiply,a*d)
    print("val from function",val)
adding()


#WAP to print even numbers between 2 and 50 also perform the addition of those even numbers.
def even_numbers():
    i=0
    sum=0
    for i in range(1,51):
        if i%2==0:
            print(i)
            sum=sum+i
    print(sum)    
even_numbers()

def odd_numbers():
    i=0
    sum=0
    for i in range (0,51):
        if i%2!=0:
            print(i)
            sum=sum+i
    print(sum)
odd_numbers()


#WAP to check given numbe is prime or not.
def prime_number(a):
    for i in range (2,int(a/2)+1):
        if a%i==0:
            print("not prime")
            return False
if prime_number(21):
    print("prime")
    
#WAP to give the multiplication table of 5,10,17.
def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} * {i} =", n*i)
    print("______________________________________")
multiplication_table(5)
multiplication_table(10)
multiplication_table(17)


  
    
        
            
            
            
        