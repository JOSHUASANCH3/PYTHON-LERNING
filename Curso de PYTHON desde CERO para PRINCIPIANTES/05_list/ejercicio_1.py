### Exercises: Level 1

#1. Declare an empty list
empty_list = list()#this is empy list
print("Ejericio 1: " + str(empty_list))
#2. Declare a list with more than 5 items
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
print("Ejercicio 2: " + str(vegetables))
#3. Find the length of your list
len_vegetables = len(vegetables)
print("Ejercicio 3: "+ str(len_vegetables))
#4. Get the first item, the middle item and the last item of the list
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
first_item = vegetables[0]#Inicio de la lista
middle_item = vegetables[len(vegetables)//2]#Usa len() para saber el total y luego lo divide para obtener la mitad
last_item = vegetables[-1]#El ultimo digido de la cadena
print("Ejercio 4:" + "\nPrimer objeto: "+ first_item + " \nSegundo Objeto: " + middle_item + " \nTercer Objeto" + last_item)
#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = list()
mixed_data_types = ['German', '24', '1.70','single', 'Managua']
#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, 
    #Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
#7. Print the list using *print()*
print("Ejercicio 5:"+ "\nFirst list: " + str(mixed_data_types) +"\nSecond List:" + str(it_companies))
#8. Print the number of companies in the list
print("Exercise 8: " + str(len(it_companies)))
#9. Print the first, middle and last company
first_it_companies = it_companies[0]
middle_it_companies = it_companies[len(it_companies)//2]
last_it_companies = it_companies[-1]
print("Ejercio 9:" + "\nPrimer objeto: "+ first_it_companies + " \nSegundo Objeto: " + middle_it_companies + " \nTercer Objeto" + last_it_companies)
#10. Print the list after modifying one of the companies
it_companies[0] = "Instagram"
print("Ejercicio 10: " + str(it_companies))
#11. Add an IT company to it_companies
it_companies.append("Facebook")
print("Ejercicio 11: " + str(it_companies))
#12. Insert an IT company in the middle of the companies list
middle_index = int(len(it_companies) / 2)
it_companies.insert(middle_index, "Youtube")
print("Ejercicio 12: " + str(it_companies))
#13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print("Ejercicio 13: " + str(it_companies))
#14. Join the it_companies with a string '#; '
separator = '#; '
joined_string = separator.join(it_companies)
print("Ejercicio 14: " + str(joined_string))
#15. Check if a certain company exists in the it_companies list.
company_name = 'Microsoft' # company to be checked
if company_name in it_companies:
    print(f"{company_name} exists in the it_companies list.")
else:
    print(f"{company_name} does not exist in the it_companies list.")
#16. Sort the list using sort() method
it_companies.sort()
print("Ejercicio 16: " + str(it_companies))
#17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print("Ejercicio 17: " + str(it_companies))
#18. Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]
print("Ejercicio 18: " + str(first_three_companies))
#19. Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print("Ejercicio 18: " + str(last_three_companies))
#20. Slice out the middle IT company or companies from the list
middle_left_index = len(it_companies) // 2 - 1
middle_right_index = len(it_companies) // 2
middle_companies = it_companies[middle_left_index:middle_right_index + 1]
print("Ejercicio 19: " + str(middle_companies))
#21. Remove the first IT company from the list
it_companies.remove(it_companies[0])
print("Ejercicio 19: " + str(middle_companies))
#?22. Remove the middle IT company or companies from the list
num_companies = len(it_companies)
if num_companies % 2 == 0:# determinar si el número de elementos en la lista es par o impar
    # si es par, eliminar las dos empresas del medio
    middle1 = int(num_companies/2 - 1)
    middle2 = int(num_companies/2)
    it_companies.pop(middle1)
    it_companies.pop(middle2-1)
else:
    # si es impar, eliminar la empresa del medio
    middle = int(num_companies/2)
    it_companies.pop(middle)
print("Exercise 22: "+ str(it_companies))
#23. Remove the last IT company from the list
it_companies.pop()
print("Exercise 23: "+ str(it_companies))
#24. Remove all IT companies from the list
it_companies =  ['Youtube', 'Oracle', 'Microsoft', 'Instagram', 'IBM', 'GOOGLE', 'Facebook', 'Apple', 'Amazon']
non_it_companies = ['Youtube', 'Oracle', 'Microsoft', 'Instagram', 'IBM', 'GOOGLE', 'Facebook', 'Apple', 'Amazon']
for company in it_companies[:]:
    if company in non_it_companies:
        it_companies.remove(company)
print("Exercise 24: "+ str(it_companies))
#25. Destroy the IT companies list
del it_companies#Se ha eliminado una lista

#26. Join the following lists:
    #front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    #back_end = ['Node','Express', 'MongoDB']`
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print("Exercise 26: "+ str(full_stack))
#27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. 
    #Then insert Python and SQL after Redux
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end
full_stack = joined_list.copy()
full_stack.insert(full_stack.index('Redux')+1, 'Python')
full_stack.insert(full_stack.index('Python')+1, 'SQL')
print("Exercise 27: "+ str(full_stack))
