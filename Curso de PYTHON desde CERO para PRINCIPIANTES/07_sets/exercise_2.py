### **💻 Exercises: Day 7**
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#!Exercises: Level 2
#1. Join A and B
C = A.union(B)
print("Exercise 1: " + str(C))
#2. Find A intersection B
D = A.intersection(D)
print("Exercise 2: " + str(C))
#3. Is A subset of B
print("Exercise 3:" + str(A.issubset(B)))
#4. Are A and B disjoint sets
print("Exercise 4:" + str(A.isdisjoint(B)))
#5. Join A with B and B with A
A.update(B)
B.update(A)
print("Exercise 5: " + "\nA: "+ A + "\nB: " + B)
#6. What is the symmetric difference between A and B
E = A.symmetric_difference(B)
print("Exercise 6: " + str(E))
#7. Delete the sets completely
del A
del B
print("Exercise 7: del A and del B")