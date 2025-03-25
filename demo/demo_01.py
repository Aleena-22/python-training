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


# Example 1: Isosceles Triangle (Only Isosceles)
x1, y1 = 0, 0
x2, y2 = 4, 0
x3, y3 = 2, 3
print("Example 1:", check_triangle(x1, y1, x2, y2, x3, y3))

# Example 2: Right-Angled Triangle (Only Right-Angled)
x1, y1 = 0, 0
x2, y2 = 3, 0
x3, y3 = 0, 4
print("Example 2:", check_triangle(x1, y1, x2, y2, x3, y3))

# Example 3: Isosceles Right-Angled Triangle (Both Isosceles and Right-Angled)
x1, y1 = 0, 0
x2, y2 = 1, 0
x3, y3 = 0, 1
print("Example 3:", check_triangle(x1, y1, x2, y2, x3, y3))

# Example 4: General Triangle (Neither Isosceles nor Right-Angled)
x1, y1 = 0, 0
x2, y2 = 2, 3
x3, y3 = 5, 4
print("Example 4:", check_triangle(x1, y1, x2, y2, x3, y3))