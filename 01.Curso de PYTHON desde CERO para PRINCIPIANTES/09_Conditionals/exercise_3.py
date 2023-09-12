"""
#?💻 Exercises 3: Day 9
Here we have a person dictionary. Feel free to modify it!

        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
"""
# Person dictionary
person = {
    'first_name': 'Joshua',
    'last_name': 'Sanchez',
    'age': 24,
    'country': 'Nicaragua',
    'is_married': True,
    'skills': ['Python', 'MySQL', 'Node.js', 'Figma', 'HTML', 'CSS'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Task 1: Check if the person dictionary has 'skills' key and print the middle skill
if 'skills' in person:
    skills_list = person['skills']
    if len(skills_list) % 2 == 1:
        middle_skill = skills_list[len(skills_list) // 2]
        print(f"The middle skill is: {middle_skill}")

# Task 2: Check if the person dictionary has 'skills' key and if 'Python' is one of the skills
if 'skills' in person and 'Python' in person['skills']:
    print("The person has Python skill.")

# Task 3: Determine the developer title based on skills
if 'skills' in person:
    skills = person['skills']
    if 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print("He is a backend developer")
    elif 'JavaScript' in skills and 'React' in skills:
        print("He is a front-end developer")
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# Task 4: Print information if married and lives in Finland
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} is married and lives in Finland.")
