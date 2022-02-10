# Data Types

# Strings
print("Hello"[-1])

# Integers 
print(123 + 456)
print(123_456 + 789) # use _ to separate numbers

# Floats
print(1.5 + 2.5)

# Boolean
True and False

# Type Conversion or Casting
num_char = len(input("Enter your name: "))
print(type(num_char))
new_num_char = str(num_char)
print(type(new_num_char))
print("Your name has " + new_num_char + " characters.")

a = float(123)
print(type(a))

a = str(123)
print(type(a))

print(float("1.5") + 10)

# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0]) + int(two_digit_number[-1]))
# or
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
result = first_digit + second_digit
print(result)

# Mathematics operations

3+2 #Add
4-1 #Subtract
2*3 #Multiply
5/2 #Divide
5**2 #Exponent

my_number = 4
my_number += 2
#result is 6

5 % 2
#result is 1


# Number Manipulation
print(round(8 / 3)) # rounds to the nearest integer
print(round(8 / 3, 2)) # rounds to 2 decimal places
print(8 // 3) # converts to integer
print(abs(- 8)) # absolute value

# F-strings
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score} and your height is {height} and you are winning is {isWinning}")
