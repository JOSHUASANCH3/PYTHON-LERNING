### Regular Expresions ###
"""
Methods in re Module
To find a pattern we use different set of re character sets that allows to search for a match in a string.

re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string
"""
#! PARAMETROS []: A set of characters
# *      [a-c] means, a or b or c
# *      [a-z] means, any letter from a to z
# *      [A-Z] means, any character from A to Z
# *      [0-3] means, 0 or 1 or 2 or 3
# *      [0-9] means any number from 0 to 9
# *      [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9

#! PARAMETROS \: uses to escape special characters
# *     \d means: match where the string contains digits (numbers from 0-9)
# *     \D means: match where the string does not contain digits
# *      any character except new line character(\n)

#! ^: starts with
# * r'^substring' eg r'^love', a sentence that starts with a word love
# * r'[^abc] means not a, not b, not c.

import re

# Prueba de re.match
my_string = "Esta es la leccion número 7: Expresiones Regulares"
my_other_string = "Esta no es la leccion número 6: Manejo de ficheros"

##? re.match: empieza a buscar desde el principio
print(re.match("Esta es la leccion", my_string, re.I))
# <re.Match object; span=(0, 18), match='Esta es la leccion'>
print(re.match("Esta es la leccion", my_other_string))
# None

##? re.match
match = re.match("Esta es la leccion", my_string, re.I)
print(match)
# <re.Match object; span=(0, 18), match='Esta es la leccion'>
start, end = match.span()
print(my_string[start:end])
# Esta es la leccion

##? re.match con if
match = re.match("Esta no es la leccion", my_other_string)
# if not(match == None): ##Otra forma de comprobar el None
# if match is not None: ##Otra forma de comprobar el None
# if match != None: ##Otra forma de comprobar el None
if not (match == None):
    print(match)
    # <re.Match object; span=(0, 21), match='Esta no es la leccion'>
    start, end = match.span()
    print(my_other_string[start:end])
    # Esta no es la leccion

# re.search
search = re.search("leccion", my_string, re.I)
if not (match == None):
    print(search)
    ## <re.Match object; span=(11, 18), match='leccion'>
    start, end = search.span()
    print(my_string[start:end])
    ## leccion

# re.findall
my_string = "Esta es la leccion número 7: Leccion llamada Expresiones Regulares"
findall = re.findall("leccion", my_string, re.I)
print(findall)
# ['leccion', 'Leccion']

# re.split: crea lista apartir de un caracter designado
print(re.split(":", my_string))

# re.sub
print(re.sub("[l|L]eccion", "LECCION", my_string, re.I))
print(re.sub("Expresiones Regulares", "RegEx", my_string, re.I))
print("\n")

# Otra forma de utilizar el re.sub
txt = """%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?"""

matches = re.sub("%", "", txt)
print(matches)
# I am teacher and  I love teaching.
# There is nothing as rewarding as educating and empowering people.
# I found teaching more interesting than any other jobs.
# Does this motivate you to be a teacher?
