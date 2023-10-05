# Greet the user
print("Hello World")
print("This is a python program")
print("What should we do next")

#Calculate Whitworth's Age
yearWhitworth = 1890
ageWhitworth = 2023 - yearWhitworth
print('Whitworth is ')
print(ageWhitworth)
print(' years old')

# Calculate Whitworth's Age
yearWhitworth = 1890
ageWhitworth = 2023-yearWhitworth
print('Whitworth is ' + str(ageWhitworth) + ' years old')

#Calculate Whitworth's Age
yearWhitworth = 1890
ageWhitworth = 2023-yearWhitworth
print(f'Whitworth is {ageWhitworth} years old')

if 5 > 2:
    print("Five is greater than two!")

    x = 4
    print (x)
    x = "Sally"
    print(x)

fruits = ["apple", "banana", "orange"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Module 1 Checkpoint Questions
# Create 3 int variables 
two = 2
four = 4
ten = 10

# Create 3 float variables
two_five = 2.5
four_five = 4.5
ten_five = 10.5

print(two + two_five)
print(ten_five - two)
print(four * two_five)
print(ten / four_five)
print(four % two)
print(ten_five % two)

#Tip Calculator
total = 47.56
print(total)
tip_10 = (total * .10)
bill = (total + tip_10)
print(tip_10) 
print(bill)
tip_15 = (total * .15)
bill = (total + tip_15)
print(tip_15)
print(bill)  
tip_20 = (total * .20)
bill = (total + tip_20)
print(tip_20) 
print(bill) 
tip_25 = (total * .25)
bill = (total + tip_25)
print("Your tip amount is " + str{tip_25})
print(bill)