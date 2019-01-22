COVERAGE = 400
length = float(input("Input length of room : "))
width = float(input("Input width of room: "))
height = float(input("Input height of room: "))
coats = int(input("How many coats of paint: "))
surface_area = 2*(length * height) + 2*(width*height) + (width * length)
coverage_needed = surface_area * coats
cans_of_paint_required = coverage_needed//COVERAGE
print("You will need " + str(cans_of_paint_required) + " cans of paint")
