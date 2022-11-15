income = [ 1000000, 17000, 500, 15000]
total = sum(income) # sum() is a built-in function
print("My total income is Rs.", total, sep="")



# Alternative way to do the same thing using a loop
expenses = [1000, 17000, 500, 150]

sum = 0 # initialize sum to 0 - here sum is a variable

for i in expenses:
    sum += i

print("I spent Rs.",sum, " on books!", sep="")



