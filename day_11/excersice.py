def add_two_function(a,b):
    return a+b
print(add_two_function(1,2))
def area_of_circle(r):
    return 3.14*r*r
print(area_of_circle(3))

def add_all_nums(*args):
    
    for types in args:
        if type(types) != int and type(types) != float:
            x = type(types)
            return(f"it is a {x} you dumbass")

    
    print("ok to proceed")
    total = 0
    for arg in args:
        total += arg

    return total  

print(add_all_nums(1, 2, 5, 2))
print(add_all_nums(5, 6, "lol", 2, 5, 2))

def convert_c_to_f(a):
    f=0
    f=((a*9)/5)+32
    return f

print(convert_c_to_f(35))
def check_season(month):
    month = month.capitalize()
    if month in ["December", "January", "February"]:
        return "Winter"
    elif month in ["March", "April", "May"]:
        return "Spring"
    elif month in ["June", "July", "August"]:
        return "Summer"
    elif month in ["September", "October", "November"]:
        return "Autumn"
    else:
        return "Invalid month"

    
print(check_season("march"))


def calculate_slope(x,y):
    if x==0:
        return("it is undefined")     
    return y/x

print(calculate_slope(7,4))

def solve_quadratic_eqn(a,b,c):
    root1=0
    root2=0
    root1=(-b-(b**2-4*a*c)**0.5)/2*a
    root2=(-b+(b**2-4*a*c)**0.5)/2*a
    return {root1,root2}
print(solve_quadratic_eqn(1,5,6))

def reverse_list(laist):
    laist.sort(reverse=True)
    return laist
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]

def add_item(laist,item):
    laist.append(item)
    return laist

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

def sum_of_numbers(a):
    total=0
    for num in range(a+1):
        total+=num
    return total    
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050


def evens_and_odds(a):
    even_list=[]
    odd_list=[]
    for num in range(a+1):
        if num%2==0:
            even_list.append(num)
        else:
         odd_list.append(num)
    return f"number of even {len(even_list)}\nnumber of odd {len(odd_list)}"      

print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.

def factorial(a):
   total=1
   for num in range(1,a+1,1):
      total=total*num
   return total  
print(factorial(5))





