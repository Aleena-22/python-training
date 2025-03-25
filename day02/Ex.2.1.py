#Write a program to calculate the height of a building given the 
#distance of the measuring instrument from the building and angle formed 
#at the observer when the highest point is seen

import math

distance = int(input("Enter the input "))
angle = int(input("Enter the angle ")) #in deg

height = distance * (math.tan(angle * (math.pi) / 180)) # in feet
height_in_metre = height * 0.3048

print(height_in_metre)

