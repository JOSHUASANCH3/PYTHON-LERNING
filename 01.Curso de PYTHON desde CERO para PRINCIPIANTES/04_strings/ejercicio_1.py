# Ejercicio_Days_4
# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print("Ejericio 1: " + "Thirty " + "Days " + "Of " + "Python")
# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print("Ejericio 2: " + "Coding " + "For " + "All")
# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
print("Ejericio 3: " + str(company))
# 4. Print the variable company using *print()*.
print("Ejericio 4: " + "Imprimir la variable 'company ' :" + company)
# 5. Print the length of the company string using *len()* method and *print()*.
len_str = len(company)
print("Ejericio 5: " + "Imprimir strings su len(): " + str(len_str))
# 6. Change all the characters to uppercase letters using *upper()* method.len
upper_str = company.upper()
print("Ejericio 6: " +"Imprimir el upper() del string: " + upper_str)
# 7. Change all the characters to lowercase letters using *lower()* method.
lower_str = company.lower()
print("Ejericio 7: " + "Imprimir el lower() :" + lower_str)
# 8. Use capitalize(), title(), swapcase() methods to format the value of the string *Coding For All*.
capitalize_str = company.capitalize()
title_str = company.title()
swapcase_str = company.swapcase()
print("Ejericio 8: " + "capitalize : " + capitalize_str + " -title : " +
      title_str + " -swapcase : " + swapcase_str)
# 9. Cut(slice) out the first word of *Coding For All* string.
slice_str = company[6:14]
print("Ejericio 9: " + "Imprimir el slice() del strings: " + slice_str)
# 10. Check if *Coding For All* string contains a word Coding using the method index, find or other methods.
index_str = company.index("Coding")
find_str = company.find("Coding")
print("Ejericio 10: " + "index: " + str(index_str) + " -find: " + str(find_str))
# 11. Replace the word coding in the string 'Coding For All' to Python.
replace_str = company.replace("Coding", "Learning")
print("Ejericio 11: " + "Remplazar la palabra 'Coding': " + replace_str)
# 12. Change Python for Everyone to Python for All using the replace method or other methods.
replace_str = company.replace("Ejericio 12: " + "Python", "Everyone")
# 13. Split the string 'Coding For All' using space as the separator (split()) .
split_str_1 = company.split()
split_str_2 = company.split(", ")
print("Ejericio 13: " + "split 1: " + str(split_str_1) + " -split2: " + str(split_str_2))
# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
number_14 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_number_14 = number_14.split(", ")
print("Ejericio 14: " + "Ejercicio 14 : " + str(split_number_14))
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
print("Ejercicio 18: ")
# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
abbreviation_str = "Coding For All"
print("Ejercicio 19: ")
# 20. Use index to determine the position of the first occurrence of C in Coding For All.
position_company = company.count("C")
print("Ejericio 20: " + str(position_company))
# 21. Use index to determine the position of the first occurrence of F in Coding For All.
position_company = company.count("F")
print("Ejericio 21: " + str(position_company))
# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
rfind_company = company.rfind("l")
print("Ejercicio 22: "+ str(rfind_company))
# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following 
      #sentence: 'You cannot end a sentence with because because because is a conjunction'.
pharse_2 = "You cannot end a sentence with because because because is a conjunction"
print("Ejercicio 23: " + str(pharse_2.index("because")))
# 24. Use rindex to find the position of the last occurrence of the word because in the following 
      #sentence: 'You cannot end a sentence with because because because is a conjunction'
last_phrase = "You cannot end a sentence with because because because is a conjunction"
print("Ejericico 24: " + str(last_phrase.rindex("because")))
# 25. Slice out the phrase 'because because because' in the following 
      #sentence: 'You cannot end a sentence with because because because is a conjunction'
slice_phrase = pharse_2[31:54]
print("Ejercicio 25: " + str(slice_phrase))
# 26. Find the position of the first occurrence of the word 'because' in the following 
      #sentence: 'You cannot end a sentence with because because because is a conjunction'
print("Ejercicio 26: " + str(pharse_2.find("because")))
# 27. Slice out the phrase 'because because because' in the following 
      #sentence: 'You cannot end a sentence with because because because is a conjunction'
slice_phrase = pharse_2[31:54]
print("Ejecicio 27: " + str(slice_phrase))
# 28. Does ''Coding For All' start with a substring *Coding*?
string = 'Coding For All'
sub_string = 'Coding'
if string.startswith(sub_string):
    print("Ejecicio 28: " + "Yes, the string starts with the sub-string.")
else:
    print("Ejecicio 28: " + "No, the string does not start with the sub-string.")
# 29. Does 'Coding For All' end with a substring *coding*?
string = 'Coding For All'
sub_string = 'Coding'
if string.endswith(sub_string):
    print("Ejecicio 29: " + "Yes, the string starts with the sub-string.")
else:
    print("Ejecicio 29: " + "No, the string does not start with the sub-string.")
# 30. ' Coding For All ' , remove the left and right trailing spaces in the given string.
string = ' Coding For All '
new_string = string.strip()
print("Ejecicio 30: " + str(new_string))
# 31. Which one of the following variables return True when we use the method isidentifier():
#   - 30DaysOfPython
#   - thirty_days_of_python
string1 = '30DaysOfPython'
string2 = 'thirty_days_of_python'
print("Ejecicio 31: " + str(string1.isidentifier())) # False
print("Ejecicio 31: " + str(string2.isidentifier())) # True
# 32. The following list contains the names of some of python 
      #libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
separator = ' # '
result = separator.join(libraries)
print("Ejecicio 32: " + str(result))

