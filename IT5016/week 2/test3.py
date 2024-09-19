txt = "find me if you can"
print(txt.rfind('i'))

print("frequency of i is:", txt.count('i'))

txt = "      kanchan      "
print(len(txt))
result = txt.strip()
print(result)
print('length of trim version:',len(result))

txt = "...rtgf.....python....rtgf...."
r = txt.strip('.rtgf')
print(r)

txt = "............rtgf....kanchan....rtgf"
l= txt.strip('.rtgf')
print(l)

strl = "hey i am kanchan"
print(strl.split())

first_name = "james"
second_name = "Bond" 
first_letter ="j"
full_name = first_letter + "." + second_name
print(full_name)

a = 3+5j
print(abs(a))

x = 200
y = 20 
print(min(x,y))
print(round(x))

print(pow(x))

a = ('hello','pinal','apple','zebra')
result = sorted(a, reverse=True)
print(result)

b = (10,20,30,40,50)
r1 = sum(b)
print(r1)








