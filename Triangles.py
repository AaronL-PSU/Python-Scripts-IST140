x=int(input("Side 1: "))
y=int(input("Side 2: "))
z=int(input("Side 3: "))

if z==y==x:
    print("Triangle is equilateral")
elif z==y or z==x or x==y:
    print("Triangle is isosceles")
elif z!=y!=x:
    print("Triangle is scalene")
