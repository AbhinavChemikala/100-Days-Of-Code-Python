
# Simple Function 
def greet():
    print("Hello")
    print("Good morning")
    print("Bye")

greet()

# Function with input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Good morning {name}")
    print(f"Bye {name}")

greet_with_name("Sam")

# Function with multiple input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What it's like in {location}")

# Positional Arguments
greet_with("Sam","India")

# Keyword Arguments
greet_with(name = "Sam",location = "India")

