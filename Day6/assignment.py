name="My Name is Pratiksha."
print(name.capitalize())              #for making only first letter capital and others are small

print(name.casefold())                #for making whole string in lower case

x=name.count("Name",1,2)              #for finding that given characters are between two given numbers
print(x)                               # it gives answers in 0 and 1 form

print(name.encode())                   # it returns encoded version of string

print(name.endswith("."))               #it returns true if string ends with specific value 

txt="H\tE\tL\tL\tO"
print(txt.expandtabs())                 #it sets whitespaces size of string
print(txt.expandtabs(2))
print(txt.expandtabs(10))


print(name.find("Pratiksha"))           #it returns values where it was found

#string format method
name="My name is Pratiksha,and I am {} years old ,I likes {},My college is {}"
print(name.format(19,"chocolate","gpp"))
