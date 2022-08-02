Name = "Shiv"
#
'''def myfunc():
  print("My name is " + name)
 
 name="abc"
 print=(name)
myfunc()
'''

def myfunc_2():
    global name
    name="abc"
    print(name)

myfunc_2()

print("my name is"+name)