# variable naming convention rules
#valid variables
myvar = "Pratiksha"
_my_var = "Pratiksha"
my_var="Pratiksha"
myVar = "Pratiksha"
MYVAR = "Pratiksha"
myvar2 = "Pratiksha"
#printing valid values
print(myvar)
print(my_var)
print(_my_var)
print(myvar)
print(MYVAR)
print(myvar2)

# invalid variable 
'''
2myvar = "Pratiksha"
my-var = "Pratiksha"
my var = "Pratiksha"
'''
#printing invalid variables
'''
print(2myvar)
print(my-var)
print(my var)
'''


#Assigning Multiple Values to Multiple Variables
print("Assigning Multiple Values to Multiple Variables")
col1, col2, col3 = "red", "orange", "green"
print(col1)
print(col2)
print(col3)

#Assigning one value  to Multiple Variables.
print("Assigning one value  to Multiple Variables.")
col1= col2= col3="red"
print(col1)
print(col2)
print(col3)

# Assigning vaules from list to variables
print("Assigning vaules from list to variables")
colors=["red","yellow","green"]
col1, col2, col3 = colors

print(col1)
print(col2)
print(col3)

# multiple variables in one statement
a="Pratiksha"
b="is"
c="Intelligent"
print(a,b,c)
print(a+b+c)

# In case of '+' operator
x = 1000
y = 10
print(x + y) 

'''x = 100
y = "Pratiksha"
print(x + y)   '''  #it gives an error