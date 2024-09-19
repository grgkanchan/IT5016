praise = "*"
repeat_1= praise * 25
first_name = "alan"
last_name = "turning"
full_name ="   " + first_name + "   " + last_name + "   "
praise = "*"
repeat_2 = praise * 25
print(repeat_1)
print(full_name)
print(repeat_2)


amount_to_convert = 500
nz_to_aus_rate = 0.95
nz_dollor = amount_to_convert

aus_dollor = nz_dollor * nz_to_aus_rate
print("NZ $" ,nz_dollor, "= AU $", aus_dollor,sep="")

aus_dollor = amount_to_convert
nz_dollor = aus_dollor / nz_to_aus_rate
print(nz_dollor)


