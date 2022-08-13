# print in lower case
name = "MY NAME IS PRATIKSHA"
print(name.lower())

# print in upper case
name = "snehal"
print(name.upper())

# print in lower case
name = "LALALALALALALALLALALALALAA"
print(name.lower())

# print a paragraph with white spaces
name = '''   this string containg whitespaces                                                                         
               but why i dont know so that  i am removing it using strip() method'''
print(name.strip())

# change one letter with another
paragraph = " hey how are you, are you doing a wrong code, oops you must be replaced by using replace() method"
print(paragraph.replace("h", "o"))


team = "hello, team, pranav, gourav, snehal, vaishnavi, pratiksha, ganesh, we must split by any operator"
print(type(team))
print(team.split(","))
team_list=team.split(",")
print(type(team_list))
print(team.split("."))


#concatenating of string
#without space
str1= "Pratiksha"
str2="Sathe"
result= str1+str2
print(result)
#with space 
space=" "
result= str1+space+str2
print(result)

#string format method
name="My name is Pratiksha,and I am {} years old ,I likes {},My college is {}"
print(name.format(19,"chocolate","gpp"))

# bool function
print(bool())
print(bool("is this true"))
print(bool(1234))
print(bool(0))
print(bool(""))

print(bool(()))
print(bool([]))
print(bool({}))
print(bool(False))
print(bool(None))









