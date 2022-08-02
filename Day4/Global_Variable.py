Name = "Pratiksha"
def myfunc():                       #function 1                   
 print(Name)
myfunc()                            #call function 1

def myfunc_2():                     #function 1                   
    global Name
    Name="Piya"
    print(Name)

myfunc_2()                          #call function 1  

print("my name is "+Name)