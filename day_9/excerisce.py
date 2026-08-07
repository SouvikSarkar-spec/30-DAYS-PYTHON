
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive")
else:
    print(f"You need {18 - age} more years to learn to drive")

if age > 25:
    diff = age - 25
    years_str = "year" if diff == 1 else "years"
    print(f"You are {diff} {years_str} older than me")
elif age < 25:
    diff = 25 - age
    years_str = "year" if diff == 1 else "years"
    print(f"You are {diff} {years_str} younger than me")
else:
    print("Same age, brother!")

# --- Section 2: Number Comparison ---
b = int(input("Enter the first number (b): "))
c = int(input("Enter the second number (c): "))

if b > c:
    print("b is greater than c")
elif b < c:
    print("b is less than c")
else:
    print("b and c are equal")

# --- Section 3: Grade Calculation ---
grade = int(input("Enter the grade: "))

if 90 <= grade <= 100:
    print("A")
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade < 80:
    print("C")
elif 60 <= grade < 70:
    print("D")
else:
    print("F")

# --- Section 4: Fruit List Modification ---
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_input = input("Fruit name is: ")

if fruit_input in fruits:
    print("It already exists in the list")
else:
    fruits.append(fruit_input)
    print(fruits)

# --- Section 5: Dictionary Skills Lookup ---
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills_list = person['skills']
    length = len(skills_list)
    
    if length % 2 == 0:
        mid2 = length // 2
        mid1 = mid2 - 1
        print("The first middle skill:", skills_list[mid1])
        print("The second middle skill:", skills_list[mid2])
    else:
        mid = length // 2
        print("The middle skill is:", skills_list[mid])
else:
    print("No skills key found in person dictionary.")

if 'skills' in person:
    skills_list=person['skills']
    if 'Python' in skills_list:
        print("the person has python skill")
    else:
        print("the person has skills but not python")
else:
    print("this person has no skills listed")   


if 'skills' in person:
    skills = set(person['skills'])

    # Exact match checks using sets
    if skills == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif skills == {'Node', 'Python', 'MongoDB'}:
        print('He is a backend developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills):
        # Using issubset allows for additional skills like JavaScript or Python to be present
        print('He is a fullstack developer')
    else:
        print('unknown title')
else:
    print('unknown title')

if person.get('is_married')==True and person.get('country') == 'Finland':
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name} is married and lives in {person['country']}.")