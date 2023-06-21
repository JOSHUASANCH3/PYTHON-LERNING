#💻 Exercises: Day 8
#Create an empty dictionary called dog
dog = {}
#Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Fido'
dog['color'] = 'brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 22,
    'marital status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}
#Get the length of the student dictionary
length = len(student)
print("Length of student dictionary:", length)
#Get the value of skills and check the data type, it should be a list
skills = student['skills']
print("Type of 'skills':", type(skills))
#Modify the skills values by adding one or two skills
student['skills'].append('HTML')
student['skills'].append('CSS')
#Get the dictionary keys as a list
keys = list(student.keys())
print("Keys:", keys)
#Get the dictionary values as a list
values = list(student.values())
print("Values:", values)
#Change the dictionary to a list of tuples using items() method
items = list(student.items())
print("Items:", items)
#Delete one of the items in the dictionary
del student['marital status']
#Delete one of the dictionaries
del dog
#Finish