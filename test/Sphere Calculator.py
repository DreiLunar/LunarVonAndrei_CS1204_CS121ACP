import math

def calculate_sphere_properties(radius):
    diameter = 2 * radius
    surface_area = 4 * math.pi * (radius ** 2)
    volume = (4/3)* math.pi * (radius ** 3)
    
    return diameter, surface_area, volume

# Calculate 
radius = float(input("Enter the radius of the sphere: "))
diameter, surface_area, volume = calculate_sphere_properties(radius)

print(f"Diameter: {diameter}")
print(f"Surface Area: {surface_area}")
print(f"Volume: {volume}")