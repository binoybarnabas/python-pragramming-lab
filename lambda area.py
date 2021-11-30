#Write lambda functions to find area of square, rectangle and triangle.

square = lambda a:a*a
rectangle = lambda l,b: l*b
triangle = lambda b,h:.5*b*h
x = int(input("enter the length of a side of the square"))
y1,y2 = int(input("enter the length of a rectangle")),int(input("enter the breadth of a rectangle"))
z1,z2 = int(input("enter the base of the triangle")),int(input("enter the height of the triangle"))
print("area of the square is",square(x))
print("area of the rectangle is",rectangle(y1,y2))
print("area of the triangle is",triangle(z1,z2))
