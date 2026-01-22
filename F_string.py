name =  "Sardar Zavian"
age = 20
print(f"my name is {name} and I am {age} years old.")



#now if i eant directly to print the string without assigning it to a variable
print(f"my name is {'Sardar Zavian'} and I am {20} years old.")
 
print(f"my name is {{'Sardar Zavian'}} and I am {{20}} years old.")

#docstring literals
def my_function():
    """This is a docstring. It is used to describe what the function does."""
    return None 
print(my_function.__doc__)  # prints the docstring of the function
 