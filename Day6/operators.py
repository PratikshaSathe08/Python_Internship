# Identity operator
print("Identity operator")
x = ["grapes", "banana"]
y = ["grapes", "banana"]
new = x
#is x and new are same
print(x is new)  
print(x is not new) 
print(x != y)
print(x is y)

#Arithmetic operator
print("\nArithmetic Operator")
a=100
b=25
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

#short hand operators
print("\nShort hand Operator")
a+=b                    #addition
print(a)

a-=b                    #substraction
print(a)

a*=b                    #multiplication
print(a)

a/=b                    #division
print(a)

#Comparison operators
print("\nComparison Operator")
x=10
y=20

print(x==y)
print(x!=y)
print(x<=y)
print(x>=y)
print(x<y)
print(x>y)

#logical operator
print("\nLogical Operator")
print(x<15 and x>5)     #and
print(x<15 and x<5)

print(x<15 or x<5)      #or
print(x<=10 or x>15)

print( not(x<15 and x>5))             #not
print( not(x>=15 and x<=5))  

#Bitwise operators
print("\nBitwise Operator")
a=10
b=4

print("a & b =",a & b)
print("a | b =",a | b)
print("~a =",~a)
print("a ^ b =",a ^ b)

#membership operator
print("\nMembership Operator")
colours=["Red","Pink","Black"]
print("Red" in colours)
print("Orange" in colours)