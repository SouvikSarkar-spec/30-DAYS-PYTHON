# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Youtube','Nvidia','Tcs'])
print(it_companies)
it_companies.pop()
print(it_companies)

C=A.union(B)
print(C)
D=A.intersection(B)
print(D)
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
E=set(age)
print(len(E)>len(age))
string='I am a teacher and I love to inspire and teach people'
words=string.split()
unique_words=set(words)
print("Number of unique words ",len(unique_words))