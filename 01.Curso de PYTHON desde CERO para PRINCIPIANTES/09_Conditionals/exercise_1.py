    #?💻 Exercises 1: Day 9
"""
#?1.Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
"""
age_interger = input("Enter your age: ");
if(age_interger > 18):
    print("You are old enough to learn to drive.");
else:
    print("You need 3 more years to learn to drive");

"""
#?2.Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
Use input(“Enter your age: ”) to get the age as input. You can use a nested condition 
to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text 
if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.
"""
my_age,your_age = null;
my_age = input("Enter my year born:");
your_age = input("Enter your year born:");
if(my_age == your_age):
    print("Our year born are different")
elif my_age > your_age:
    print("Im more years old than you");
else:
    print("Our year birn are same");

"""
#?3.Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3
"""
number_a = input("Enter the number A:");
number_b = input("Enter the number B:");
if(number_a > number_b):
    print(number_a+" is greater than "+number_b);
elif(number_a < number_b):
    print(number_a+" is smaller than "+number_b);
else:
    print(number_a+" is equal than "+number_b);