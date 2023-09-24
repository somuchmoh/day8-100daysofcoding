# Review: 
# Create a function called greet(). Write 3 print statements inside the function. Call the greet() 
def greet():
    print("Hello!")
    print("Hope you are well!")
    print("Bye")

greet()

#Function with inputs 
def greet_with_name(name):
    print(f"Hello, {name}")
    print(f"Hope you are well, {name}!")

greet_with_name("Mohana")

#Functions with multiple inputs
def greet_with_inputs(name, location):
    print(f"Hey, {name}")
    print(f"How is the weather in {location}?")

greet_with_inputs("Mohana", "Bangalore")

#Calling function with keyword arguments 
greet_with_inputs(location="Bangalore", name = "Mohana")