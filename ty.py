shape = input().strip().lower()

if shape == "rectangle":
    width = float(input())
    height = float(input())
    area = width * height

elif shape == "triangle":
    base = float(input())
    height = float(input())
    area = (base * height) / 2

elif shape == "circle":
    radius = float(input())
    area = 3.14159 * radius * radius

print("Area:", area)