### **💻 Exercises: Day 7**
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#!Exercises: Level 3
#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print("Exercise 1: " + "\nAge len: " + str(len(age)) + "\nAge set: " + len(age_set))
#2. Explain the difference between the following data types: string, list, tuple and set
"""
String: A string is a sequence of characters enclosed in quotes. It is an immutable data type, 
which means that once created, it cannot be modified. Strings are often used to store text and are 
indexed starting from 0.

List: A list is a collection of items enclosed in square brackets and separated by commas. 
Lists are mutable, which means that they can be modified after creation. Lists are ordered and indexed 
starting from 0.

Tuple: A tuple is a collection of items enclosed in parentheses and separated by commas. 
Tuples are immutable, which means that they cannot be modified after creation. Tuples are ordered and 
indexed starting from 0.

Set: A set is a collection of unique items enclosed in curly braces and separated by commas. 
Sets are mutable, and they can be modified after creation. Sets are unordered, and they do not 
support indexing.
"""
#3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
words = sentence.split()
unique_words = set(words)
print("Exercise 3: " + str(len(unique_words)))