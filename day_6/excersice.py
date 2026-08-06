tup=()
brother=("John", "Mike", "David")
sister=("Emily", "Sarah", "Lisa")
siblings=brother+sister
print(siblings)
count=len(siblings)
print(count)
parents=("Robert", "Linda")
family_members=parents+siblings
print(family_members)


a,b,c,d,e,f,g,h=family_members
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
fruits=("apple","banana","cherry")
animal_products=("milk","cheese","butter")
vegetables=("carrot","broccoli","spinach")
food_stuff_tp=fruits+animal_products+vegetables
print(food_stuff_tp)
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)
len_food=len(food_stuff_lt)
print(len_food)
middle_part=food_stuff_lt[len_food//2:len_food//2+1]
print(middle_part)
first_three=food_stuff_lt[0:3]
last_three=food_stuff_lt[-3:]
print(first_three)
print(last_three)
nordic_countries =('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
del food_stuff_tp     #I know this will crash as it is mentioned if anybody want to run my code remove last two section
"milk" in food_stuff_tp

