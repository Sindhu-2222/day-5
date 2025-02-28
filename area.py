import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python3 area.py <side1> <side2>")
    sys.exit(1)

# Read sides from command-line arguments
side1 = float(sys.argv[1])
side2 = float(sys.argv[2])

# Calculate area
area = side1 * side2
print(f"The area of the rectangle is: {area}")
