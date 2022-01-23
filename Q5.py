def area_of_triangle(x,y,z):
    s= 0.5*(x+y+z)                        #semiperimeter of triangle
    area = (s*(s-x)*(s-y)*(s-z))**(0.5)           #area using Heron's formula
    print(area, "square units")
area_of_triangle(4,3,2)    
