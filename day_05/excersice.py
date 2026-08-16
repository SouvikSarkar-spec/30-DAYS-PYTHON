# Section 1: Basic Lists
first_list = []
second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

length = len(second_list)
first_item = second_list[0]
middle_item = second_list[length // 2]
last_item = second_list[-1]

print(second_list)

# Section 2: IT Companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

nvidia = it_companies[5]
meta = it_companies[len(it_companies) // 2]

it_companies[0] = 'FACEBOOK'
new_it_companies = '#; '.join(it_companies)
print(new_it_companies)

print(it_companies.index('Apple'))

it_companies.sort()
print(it_companies)

print(it_companies[0:3])
print(it_companies[-3:])

it_companies.clear()
print(it_companies)
del it_companies

# Section 3: Tech Stack
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

new_stack = front_end + back_end
full_stack = new_stack.copy()

a = full_stack.index('Redux')
full_stack.insert(a + 1, 'Python')
full_stack.insert(a + 2, 'SQL')

print(full_stack)

# Section 4: Ages Statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min_age = ages[0]
max_age = ages[-1]

print("min age:", min_age)
print("max age:", max_age)

ages.append(max_age)
ages.append(min_age)
ages.sort()

# Median of updated list
median_age = (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2
print("median age:", median_age)

avg_age = sum(ages) / len(ages)
print("average age:", avg_age)

min_age_diff = abs(min_age - avg_age)
max_age_diff = abs(max_age - avg_age)
print("bigger is:", min_age_diff > max_age_diff)

# Section 5: Countries
countries = [
  'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
  'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
  'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan',
  'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria',
  'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada',
  'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros',
  'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica',
  "Côte d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark',
  'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor-Leste)',
  'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
  'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia',
  'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau',
  'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran',
  'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan',
  'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan',
  'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
  'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
  'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico',
  'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco',
  'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand',
  'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan',
  'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru',
  'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda',
  'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines',
  'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal',
  'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
  'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka',
  'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania',
  'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
  'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
  'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu',
  'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
]

total_countries = len(countries)
print("Total countries:", total_countries)

middle_index = total_countries // 2
print("Middle country:", countries[middle_index])

half_point = (total_countries + 1) // 2
first_half = countries[:half_point]
second_half = countries[half_point:]

first, second, third, *scandic_countries = countries