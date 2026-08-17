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
