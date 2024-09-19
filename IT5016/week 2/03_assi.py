"""
calculating the person's age 
Author : Kanchan
"""
name = input("what is your name:")
date_of_birth =int(input("what is your birth date:"))
current_year = int(input("current_year:"))
current_age =current_year - date_of_birth
print("hey",name,"you are now",current_age,"W0w!",)



a = 42
b = 3.14
c = "Hello,World"
d = [1,2,3]
e = (1,2)
f ={"name":"john","age":30}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

b = 3.14
string_value = str(b)
print(string_value)
print(type(string_value))
