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
print("Ejercio 4:" + first_item + " " + middle_item + " " + last_item)
#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, 
    #Oracle and Amazon.
#7. Print the list using *print()*
#8. Print the number of companies in the list
#9. Print the first, middle and last company
#10. Print the list after modifying one of the companies
#11. Add an IT company to it_companies
#12. Insert an IT company in the middle of the companies list
#13. Change one of the it_companies names to uppercase (IBM excluded!)
#14. Join the it_companies with a string '#; '
#15. Check if a certain company exists in the it_companies list.
#16. Sort the list using sort() method
#17. Reverse the list in descending order using reverse() method
#18. Slice out the first 3 companies from the list
#19. Slice out the last 3 companies from the list
#20. Slice out the middle IT company or companies from the list
#21. Remove the first IT company from the list
#22. Remove the middle IT company or companies from the list
#23. Remove the last IT company from the list
#24. Remove all IT companies from the list
#25. Destroy the IT companies list
#26. Join the following lists:
    #front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    #back_end = ['Node','Express', 'MongoDB']`
#27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. 
    #Then insert Python and SQL after Redux