import random
import string
def random_user_id():
 x=string.ascii_letters+ string.digits
 z=""
 for o in range(6):
    y=random.choice(x)
    z+=y

 return z

def user_id_gen_by_user():
  x=int(input("number of character is "))
  y=int(input("number of ids is "))
  a=string.ascii_letters+ string.digits
  z=""
  for u in range(y):
   for o in range(x):
      b=random.choice(a)
      z+=b
   z+="\n"  
  return f"{z}"


print(user_id_gen_by_user()) # user input: 5 5


def rgb_color_gen():
  x=random.randint(0,255)
  y=random.randint(0,255)
  z=random.randint(0,255)
  return x,y,z

print(rgb_color_gen())

def list_of_hexa_colors(x):
  z=string.digits
  y='abcdef'
  lst=[]
  for o in range(x):
    i=""
    for o in range(6):
          b=random.choice(z+y)
          i+=b
    i='#'+i
    lst.append(i)
  return f"{lst}"

print(list_of_hexa_colors(5))

def list_of_rgb(x):
 lst=[]
 for o in range(x):
     a=random.randint(0,255)
     y=random.randint(0,255)
     z=random.randint(0,255)
     lst.append(f"rgb({a},{y},{z})")

 return lst
print(list_of_rgb(5))

def generate_colors(type,x):
  if type=='hexa':
    return list_of_hexa_colors(x)
  else:
    return list_of_rgb(x)

print(generate_colors('hexa',5)) 

def shuffle_list(a):
  b=a.copy()
  random_list=[]
  for x in range(len(a)):
    y=random.choice(b)
    random_list.append(y)
    b.remove(y)
  return random_list

print(shuffle_list([1,5,6,3,6,7]))

def seven_random_numbers():
  a=[]
  num=0
  while len(a)<7:
    num=random.randint(0,9)
    if num not in a:
      a.append(num)
    else:
      continue
  return a

print(seven_random_numbers())
  

 