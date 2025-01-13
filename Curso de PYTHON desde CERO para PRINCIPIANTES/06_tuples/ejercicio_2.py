### Exercises: Level 2 ###
#Unpack siblings and parents from family_members
family_members = ('John', 'Jack', 'Jane', 'Jennifer', 'Father', 'Mother')
siblings, parents = family_members[:4], family_members[4:]
#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
variable called food_stuff_tp.
fruits = ('banana', 'apple', 'kiwi')
vegetables = ('carrot', 'potato', 'onion')
animal_products = ('milk', 'cheese', 'meat')
food_stuff_tp = fruits + vegetables + animal_products
#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_tp) // 2
middle_item = food_stuff_tp[middle_index]
middle_items = food_stuff_tp[middle_index-1:middle_index+1]
middle_item_lt = food_stuff_lt[middle_index]
middle_items_lt = food_stuff_lt[middle_index-1:middle_index+1]
#Slice out the first three items and the last three items from food_staff_lt list
first_three_items_lt = food_stuff_lt[:3]
last_three_items_lt = food_stuff_lt[-3:]
#Delete the food_staff_tp tuple completely
del food_stuff_tp
#Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
#Check if 'Estonia' is a nordic country and nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
