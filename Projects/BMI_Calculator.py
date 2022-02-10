# calculate bmi and print the result

height = (input("enter your height in m: "))
weight = (input("enter your weight in kg: "))

bmi = int(weight)/(float(height)*float(height))
print(int(bmi))