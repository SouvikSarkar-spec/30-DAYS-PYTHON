numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
lst=[i for i in numbers if i<=0]
print(lst)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst_1=[item for sublist in list_of_lists for item in sublist]
print(lst_1)

lst_2=[(i,1,i,i**2,i**3,i**4,i**5) for i in range(11)]
print(lst_2)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lst_3=[list(item) for sublist in countries for item in sublist]
print(lst_3)
lst_4=[(country.upper(),country[:3].upper(),capital.upper()) for [(country,capital)] in countries]
print(lst_4)
lst_5=[{'country':a,'city':b} for [(a,b)] in countries]
print(lst_5)
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
lst_6=[name+' '+surname for [(name,surname)] in names]
print(lst_6)

def ans(type):
     type=type.capitalize()
     if type=="Slope":
          return lambda x,y,x_1,y_1:(y_1-y)/(x_1-x)
     return lambda x,y,x_1,y_1:y-((y_1-y)/(x_1-x))*x
print(ans("slope")(1,2,5,6))
          