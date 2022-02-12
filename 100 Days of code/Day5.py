# for loops 
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) 
'''
# Average height of people in a class
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total = 0
count = 0
for height in student_heights:
    total += height
    count += 1

average = total / count
print(round(average))

# Another way to do this is to use the sum() and len() methods.
average = sum(student_heights) / len(student_heights)
print(round(average))
'''
# For loops with Range
for number in range(1, 11):
    print(number)

# For loops with Range and Step
for number in range(1, 11, 2):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)

# Adding only even numbers in a range of 1 to 100
total = 0
for number in range(2, 101, 2):
    total += number
print(total)

# FizzBuzz - Print numbers from 1 to 100. For multiples of 3, print "Fizz". For multiples of 5, print "Buzz". For multiples of 3 and 5, print "FizzBuzz".
#Write your code below this row 👇

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)