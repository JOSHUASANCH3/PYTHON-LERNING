# **💻 Exercises: Day 7**
# sets
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#!Exercises: Level 1
# 1. Find the length of the set it_companies
len_companies = str(len(it_companies))
len_a = str(len(A))
len_b = str(len(B))
len_age = str(len(age))
print("Exercise 1: " + )  # Output: 7

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("Exercise 2: " + str(it_companies))

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Tesla', 'Uber', 'SpaceX'])
print("Exercise 3: " + str(it_companies))
# 4. Remove one of the companies from the set it_companies
it_companies.remove('Uber')
print("Exercise 4: " + str(it_companies))
# 5. What is the difference between remove and discard
    # The remove() method raises a KeyError if the specified element doesn't exist in the set,
    # whereas the discard() method doesn't raise any error if the specified element doesn't exist.
it_companies.discard('Twitter')
print("Exercise 5: " + str(it_companies))