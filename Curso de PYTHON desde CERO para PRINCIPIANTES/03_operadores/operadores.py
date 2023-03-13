# Booleanos
# A boolean data type represents one of the two values: True or False
print(True)
print(False)

# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
# 2.0  Division in Python gives floating number
print('Division: ', 4 / 2)
print('Division: ', 6 / 2)        # 3.0
print('Division: ', 7 / 2)        # 3.5
# 3,  gives without the floating number or without the remaining
print('Division without the remainder: ', 7 // 2)
print('Division without the remainder: ', 7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3)  # 9 it means 2 * 2 * 2

# Ejemplo de comparadores aritmétricos
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

"""
In addition to the above comparison operator Python uses:

- *is*: Returns true if both variables are the same object(x is y)
- *is not*: Returns true if both variables are not the same object(x is not y)
- *in*: Returns True if the queried list contains a certain item(x in y)
- *not in*: Returns True if the queried list doesn't have a certain item(x in y)
"""
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh')  # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh')  # False - there is no uppercase B
# True - because coding for all has the word coding
print('coding' in 'coding for all')
print('a in an:', 'a' in 'an')       # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# Operadores Logicos
print(3 > 2 and 4 > 3)  # True - because both statements are true
print(3 > 2 and 4 < 3)  # False - because the second statement is false
print(3 < 2 and 4 < 3)  # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False)  # False
