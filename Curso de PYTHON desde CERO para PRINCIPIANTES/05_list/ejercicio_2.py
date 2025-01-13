"""

()
2. Divide the countries list into two equal lists if it is even if not one more country for the first half.

"""
#1. The following is a list of 10 students ages:
#?ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]`
#!- Sort the list and find the min and max age
#!- Add the min age and the max age again to the list
#!- Find the median age (one middle item or two middle items divided by two)
#!- Find the average age (sum of all items divided by their number )
#!- Find the range of the ages (max minus min)
#!- Compare the value of (min - average) and (max - average), use *abs()* method
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#1.1. Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
#1.2. Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
#1.3. Find the median age
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2] + ages[n//2-1])/2
else:
    median_age = ages[n//2]
#1.4. Find the average age
average_age = sum(ages)/n
#1.5. Find the range of the ages
age_range = max_age - min_age
#1.6. Compare the value of (min - average) and (max - average)
diff_min = abs(min_age - average_age)
diff_max = abs(max_age - average_age)
#1.7. Print the results
print("Sorted ages:", ages)
print("Minimum age:", min_age)
print("Maximum age:", max_age)
print("Median age:", median_age)
print("Average age:", average_age)
print("Age range:", age_range)
print("Absolute difference between min and average ages:", diff_min)
print("Absolute difference between max and average ages:", diff_max)

#2. Find the middle country(ies) in the [countries list]
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka','Sudan', 'Suriname', 'Swaziland',  'Sweden', 'Switzerland',  'Syria', 'Taiwan','Tajikistan',  'Tanzania','Thailand',  'Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Uzbekistan','Vanuatu','Vatican City','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe'];
middle_countries_1 = len(countries) // 2 - 1
middle_countries_2 = len(countries) // 2
middle_countries_ = countries[middle_countries_1:middle_countries_2 + 1]
print("Exercise 2: " + str(middle_countries_))

#3 Divide the countries list into two equal lists if it is even if not one more country for the first half.
length = len(countries)#? Determine the length of the list
midpoint = length // 2#? Calculate the midpoint of the list
first_half = countries[:midpoint]#? Split the list into two equal halves
second_half = countries[midpoint:]
print("Exercise 3: " + "\nFirst half:" + str(first_half) + "\nSecond half: " + str(second_half))
#4. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
china, russia, usa, *scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']