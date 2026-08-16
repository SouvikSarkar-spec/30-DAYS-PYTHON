statement="Coding For All"
print(statement[0:6])

statement="Coding For All"
print(statement.index("Coding"))
print(statement.find("Coding"))
print(statement.replace("Coding", "Python"))
print(statement.split(" "))
statement="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(statement.split(", "))
statement="Coding For All"
print(statement[0])
last_index=len(statement)-1
print(last_index)
statement="  Coding For All  "
print(statement.strip())
radius=10
area=3.14*radius**2
print(f"The area of a circle with radius {radius} is {area}.")