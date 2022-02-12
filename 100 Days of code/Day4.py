import random

random_int = random.randint(0,10) 
print(random_int) # This will print a random integer between 0 and 10

random_float = random.random()
print(random_float) # This will print a random float between 0 and 1

random_float = random.uniform(0,10)
print(random_float) # This will print a random float between 0 and 10

cars = ["Ford", "Volvo", "BMW"]
random_choice = random.choice(cars) # This will print a random element from the list

# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits) # Prints the whole list
print(fruits[1]) # Prints the second element of the list
fruits[1] = "kiwi" # Change the value of the second element
fruits.append("orange") # Add to the end of the list
fruits.insert(1, "pear") # Inserts at index 1
fruits.remove("banana") # Removes the first instance of the item
fruits.pop() # removes last item
fruits.pop(1) # Remove the item at index 1
fruits.clear() # removes all elements from the list
fruits.sort() # alphabetical
fruits.reverse() # reverse the order of the list
fruits.index("apple") # Returns the index of the first instance of the value
fruits.count("apple") # Counts how many times the item appears in the list
fruits.extend(["orange", "pear"]) # Add list to list