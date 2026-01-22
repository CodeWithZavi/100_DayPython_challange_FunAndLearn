# # name =  "Sardar Zavian"
# # age = 20
# # print(f"my name is {name} and I am {age} years old.")



# # #now if i eant directly to print the string without assigning it to a variable
# # print(f"my name is {'Sardar Zavian'} and I am {20} years old.")
 
# # print(f"my name is {{'Sardar Zavian'}} and I am {{20}} years old.")

# # #docstring literals
# # def my_function():
# #     """This is a docstring. It is used to describe what the function does."""
# #     return None 
# # print(my_function.__doc__)  # prints the docstring of the function

# # #how docstring change the program behavior
# # def add(a, b):  
# #     """Returns the sum of a and b."""
# #     return a + b
# # print(add(3, 5))  # prints 8
# # print(add.__doc__)  # prints the docstring of the function
# # #where program change 

# #an example that doc string can change the program and comment cannot
# def multiply(a, b):
#     """Returns the product of a and b."""
#     return a * b
# print(multiply(4, 6))  # prints 24
# print(multiply.__doc__)  # prints the docstring of the function
# help(multiply)  # provides detailed information about the function, including its docstring
# #without docstring help function will not provide any information

