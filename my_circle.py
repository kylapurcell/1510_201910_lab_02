PI = 3.14159
radius = 0
radius =float(input("Input the radius: "))
double_radius = 2*radius
circumference = 2*PI*radius
print(circumference)
area = PI*radius*radius
print(area)
double_radius_circumference = 2*PI*double_radius
double_radius_area = PI*double_radius*double_radius
how_much_bigger_circumference = double_radius_circumference//circumference
how_much_bigger_area = double_radius_area//area
string1 = "The circumference is " + str(how_much_bigger_circumference) + " times bigger when the radius is doubled " \
 + "and the area is " + str(how_much_bigger_area) + " bigger when the radius is doubled"
print(string1)
