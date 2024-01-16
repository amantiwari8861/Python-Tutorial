# Scope in Python refers to the region or context in which a variable or object is visible and can be accessed.

# Local Scope (L): Variables defined within a function are local to that function. They are not accessible outside the function.
# def example_function():
#     local_variable = 10

# Enclosing Scope (E): If a function is defined inside another function, the inner function has access to variables in the outer (enclosing) function.
# def outer_function():
#     outer_variable = 20
#     def inner_function():
#         print(outer_variable)

# Global Scope (G): Variables defined at the top level of a script or module are considered global. They are accessible throughout the module.
# global_variable = 30

# Built-in Scope (B): This includes Python's built-in functions and constants like print(), len(), and True.
# print(len("example"))

# LEGB Rule:
# LEGB stands for Local, Enclosing, Global, and Built-in. It's a rule that defines the order in which Python searches for names (variables or objects).

# Local (L): Python looks for the name in the local scope (inside the current function).
# Enclosing (E): If the name is not found locally, Python looks in the enclosing scopes (if the function is defined inside another function).
# Global (G): If the name is still not found, Python looks in the global scope (at the top level of the module).
# Built-in (B): If the name is not found in any of the above, Python looks in the built-in scope (Python's built-in functions and objects).