import math

# Function to calculate distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to check triangle type
def check_triangle(x1, y1, x2, y2, x3, y3):
    # Step 1: Calculate distances AB, BC, CA
    AB = distance(x1, y1, x2, y2)
    BC = distance(x2, y2, x3, y3)
    CA = distance(x3, y3, x1, y1)
    
    # Step 2: Check if the triangle is isosceles
    is_isosceles = (AB == BC) or (BC == CA) or (CA == AB)
    
    # Step 3: Check if the triangle is right-angled (Pythagorean theorem)
    sides = [AB, BC, CA]
    sides.sort()
    # Check if square of the largest side equals sum of the squares of the other two sides
    is_right_angled = (math.isclose(sides[2]**2, sides[0]**2 + sides[1]**2))
    
    # Step 4: Determine the result
    if is_isosceles and is_right_angled:
        return "Isosceles Right-Angled Triangle"
    elif is_isosceles:
        return "Isosceles Triangle"
    elif is_right_angled:
        return "Right-Angled Triangle"
    else:
        return "General Triangle"

# Taking user input for the coordinates of points A, B, and C
print("Enter the coordinates of point A (x1, y1): ")
x1, y1 = float(input("x1: ")), float(input("y1: "))

print("Enter the coordinates of point B (x2, y2): ")
x2, y2 = float(input("x2: ")), float(input("y2: "))

print("Enter the coordinates of point C (x3, y3): ")
x3, y3 = float(input("x3: ")), float(input("y3: "))

# Check the type of triangle
result = check_triangle(x1, y1, x2, y2, x3, y3)
print(f"The triangle is: {result}")