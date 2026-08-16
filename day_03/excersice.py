
age=19
height=5.6
complex=1+2j
base=int(input("Enter the base: "))
height=int(input("Enter the height: "))
area=0.5*base*height
print("The area of the triangle is:", area)

side_a=int(input("Enter the length of side a: "))
side_b=int(input("Enter the length of side b: "))   
side_c=int(input("Enter the length of side c: "))
perimeter=side_a+side_b+side_c
print("The perimeter of the triangle is:", perimeter)

length=int(input("Enter the length of the rectangle: "))
width=int(input("Enter the width of the rectangle: "))
area_rectangle=length*width
perimeter_rectangle=2*(length+width)
print("The area of the rectangle is:", area_rectangle)
print("The perimeter of the rectangle is:", perimeter_rectangle)

radius=int(input("Enter the radius of the circle: "))
area_circle=3.14*radius**2
circumference_circle=2*3.14*radius
print("The area of the circle is:", area_circle)
print("The circumference of the circle is:", circumference_circle)

slope=2
y_intercept=2*0-2 #as at intercept, x=0
x_intercept=(0+2)/2 #as at intercept, y=0 #Dividing gives float value
print("The slope is:", slope)
print("The y-intercept is:", y_intercept)
print("The x-intercept is:", x_intercept)  


y2, y1, x2, x1 = 10, 2, 6, 2
euclidean_distance=((x2-x1)**2+(y2-y1)**2)**0.5
print("The slope using the formula is:", slope_distance)
print("The Euclidean distance is:", euclidean_distance)

print("The slope is greater than slope_distance: ", slope > slope_distance)

x=0
y=x**2 + 6*x + 9
print("The value of y when x=0 is:", y)
x=-3
y=x**2 + 6*x + 9
print("The value of y when x=-3 is:", y)

print(not(len("python") == len("dragon")))

print("on" in "python" and "on" in "dragon") 

print("jargon" in "I hope this course is not full of jargon.")

print("on" not in "python" and "on" not in "dragon")

len_python=float(len("python"))
len_string=str(len)
print("The length of the string 'python' is:", len_string)

number=int(input("Enter a number: "))
print("The number is even:", number % 2 == 0)
print("The number is odd:", number % 2 != 0)

print(7//3 == int(2.7))

print(type('10') == type(10))

print(int(9.8) == 10)

hours=int(input("Enter hours: "))
rate=int(input("Enter rate per hour: "))
print("The weekly earning is:", hours * rate)

years=int(input("Enter number of years you have lived: "))
print("You have lived for", years * 365 * 24 * 60 * 60, "seconds.")

print("1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")