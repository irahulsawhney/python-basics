# This is a single-line comment in Python.

'''
This is a
multi-line comment in Python.
'''
"""
This is another
multi-line comment in Python.
"""

print("Hello, and welcome to the Python World!")

if 5 > 2:
    print("Five is indeed greater than two!") # this belongs to the if block
print("End of program") # this does not belong to the if block


"""
Testing different print variants
"""
print("Hello, world!") # prints a constant string
print(5) # prints a constant number
x = 10   # defines a variable
print(x) # prints a variable
print(3 * 7) # prints the result of an expression - 21

# The next line prints: "Cosmo can make you 10 times more effective!" - Note that this adds a space before and after x
print("Cosmo can make you", x, "times more effective!") # Combine the text and a variable

my_variable = "Hello, world!"
print(my_variable) # This will print "Hello, world!"

my_variable = 123
print(my_variable) # This will print 123

# This section is about variables. Note that Python variables can also be named starting _
x = 7 # valid: starts with a letter
myVariable = 7 # valid: starts with a letter
_myVariable = 7 # valid: starts with an underscore
# 7x = 7 # invalid - starts with a digit
# x!y = 7 # invalid - contains the prohibited character '!'

# We are in ancient Egypt, and we see a hieroglyph, which is a series of numbers.
# Let's decode this hieroglyph using Python variables

hieroglyph = 1290 # The hieroglyph in numerical form we found in the pyramid
year_discovered = "2022 A.D." # The year we discovered the hieroglyph

print("The hieroglyph discovered in", year_discovered, "translates to the year", hieroglyph, "B.C. in the Egyptian calendar.")

# We need to add another Pharaoh to our exhibit
# Use the right variables and print function to complete the code

pharaoh = "Pharaoh Ramses II"
# Pharaoh's Ramses II reign was from 1279 BC to 1213 BC
reign = "1279 BC to 1213 BC"
print(pharaoh, "ruled during", reign)

"""Start with Boolean comparison operations"""
price_of_toy = 15
money_in_hand = 20

# Compare two variables and assign the result to a new variable
can_buy_toy = money_in_hand >= price_of_toy
print("Can buy toy?", can_buy_toy)  # Prints: True

print(10 == 100/10)  # True - because 10 is indeed equal to 10
print(10 > 10)   # False - because 10 isn't greater than 10
print(10 < 10)   # False - because 10 isn't less than 10
print(10 != 10)  # False - because 10 isn't unequal to 10
print(10 >= 10)  # True - because 10 is equal to 10
print(10 <= 10)  # True - because 10 is equal to 10

