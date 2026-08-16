dog={}
dog['name']='dog'
dog['color']='white'
dog['legs']=4
dog['age']=2
dog['breed']='husky'
student={
    'first_name':'jane',
    'last_name':'doe',
    'gender':'female',
    'age':19,
    'marital_status':'not',
    'skills':['robbing','seduction','loving'],
    'country':'imagination',
    'city':'anime',
    'address':'my heart'
}
print(len(student))
value=student['skills']
print(type(student['skills']))
print(value)
student['skills'].extend(['imaginary','backstabbing'])
print(type(student['skills']))
keys=list(student.keys())
print(keys)
values=list(student.values())
print(values)
print(student.items())
del student['skills']
del dog

