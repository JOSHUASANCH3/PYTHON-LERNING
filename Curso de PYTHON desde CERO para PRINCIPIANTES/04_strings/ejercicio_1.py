# Ejercicio_Days_4
# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print("Thirty " + "Days " + "Of " + "Python")
# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print("Coding " + "For " + "All")
# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
# 4. Print the variable company using *print()*.
print("Imprimir la variable 'company ' :" + company)
# 5. Print the length of the company string using *len()* method and *print()*.
len_str = len(company)
print("Imprimir strings su len(): " + str(len_str))
# 6. Change all the characters to uppercase letters using *upper()* method.len
upper_str = company.upper()
print("Imprimir el upper() del string: " + upper_str)
# 7. Change all the characters to lowercase letters using *lower()* method.
lower_str = company.lower()
print("Imprimir el lower() :" + lower_str)
# 8. Use capitalize(), title(), swapcase() methods to format the value of the string *Coding For All*.
capitalize_str = company.capitalize()
title_str = company.title()
swapcase_str = company.swapcase()
print("capitalize : " + capitalize_str + " -title : " +
      title_str + " -swapcase : " + swapcase_str)
# 9. Cut(slice) out the first word of *Coding For All* string.
slice_str = company[6:14]
print("Imprimir el slice() del strings: " + slice_str)
# 10. Check if *Coding For All* string contains a word Coding using the method index, find or other methods.
index_str = company.index("Coding")
find_str = company.find("Coding")
print("index: " + str(index_str) + " -find: " + str(find_str))
# 11. Replace the word coding in the string 'Coding For All' to Python.
replace_str = company.replace("Coding", "Learning")
print("Remplazar la palabra 'Coding': " + replace_str)
# 12. Change Python for Everyone to Python for All using the replace method or other methods.
replace_str = company.replace("Python", "Everyone")
# 13. Split the string 'Coding For All' using space as the separator (split()) .
split_str_1 = company.split()
split_str_2 = company.split(", ")
print("split 1: " + str(split_str_1) + " -split2: " + str(split_str_2))
# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
number_14 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_number_14 = number_14.split(", ")
print("Ejercicio 14 : " + str(split_number_14))
# 15. What is the character at index 0 in the string *Coding For All*.
first_word = company[0]
print("Ejercicio 15: " + first_word)
# 16. What is the last index of the string *Coding For All*.
last_index = len(company) - 1
last_word = company[last_index]
print("Ejercicio 16: " + last_word)
# 17. What character is at index 10 in "Coding For All" string.
ten_word = company[10]
print("Ejercicio 17: " + ten_word)#?EL valor es un espacio
# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym_str = "Python For Everyone"
# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
abbreviation_str = "Coding For All"
# 20. Use index to determine the position of the first occurrence of C in Coding For All.

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'.
# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 28. Does ''Coding For All' start with a substring *Coding*?
# 29. Does 'Coding For All' end with a substring *coding*?
# 30. ' Coding For All ' , remove the left and right trailing spaces in the given string.
# 31. Which one of the following variables return True when we use the method isidentifier():
#   - 30DaysOfPython
#  - thirty_days_of_python
# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
