    #?💻 Exercises 2: Day 9
"""
#? 1.Write a code which gives grade to students according to theirs scores:

90-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""
scores_students = input("Ingresive your score");
if(scores_students >= 90 && scores_students =< 100):
    print('Your score is "A"')
elif(scores_students >= 70 && scores_students =< 89):
    print('Your score is "B"')
elif(scores_students >= 60 && scores_students =< 69):
    print('Your score is "C"')
elif(scores_students >= 50 && scores_students =< 59):
    print('Your score is "D"')
elif(scores_students >= 0 && scores_students =< 49):
    print('Your score is "F"')

"""
#? 2.Check if the season is Autumn, Winter, Spring or Summer. If the user input is: 
#   September, October or November, the season is Autumn. 
#   December, January or February, the season is Winter. 
#   March, April or May, the season is Spring. 
#   June, July or August, the season is Summer.
"""
# Define lists of months for each season
autumn_months = ["september", "october", "november"]
winter_months = ["december", "january", "february"]
spring_months = ["march", "april", "may"]
summer_months = ["june", "july", "august"]

# Get the month from the user
month = input("Enter a month: ").lower()

# Determine the season
if month in autumn_months:
    season = "Autumn"
elif month in winter_months:
    season = "Winter"
elif month in spring_months:
    season = "Spring"
elif month in summer_months:
    season = "Summer"
else:
    season = "Unknown"

# Display the result
if season != "Unknown":
    print(f"The season for {month.capitalize()} is {season}.")
else:
    print("Invalid input. Please enter a valid month.")

"""
#? 3.The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
->  If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
    If the fruit exists print('That fruit already exist in the list')
"""
# List of fruits
fruits = ['banana', 'orange', 'mango', 'lemon']

# Ask the user for a fruit
fruit = input("Enter a fruit: ").lower()

# Check if the fruit is already in the list
if fruit in fruits:
    print(f"{fruit.capitalize()} already exists in the list.")
else:
    # Add the fruit to the list
    fruits.append(fruit)
    print(f"{fruit.capitalize()} has been added to the list.")

# Print the modified list of fruits
print("Updated list of fruits:", fruits)
