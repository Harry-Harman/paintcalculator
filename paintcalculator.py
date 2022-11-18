import math

def area(w, h):
    return w * h


def desired_colour():
    colour = (input("What colour of paint would you like to use on this wall? "))
    colour_needed.append(colour.upper())


def wall_obstructions(obst):
    i = 1
    obstructions_list = []
    while i <= obst:
        ob_width = float(input(f"What is the width of obstruction {i}? "))
        ob_height = float(input(f"What is the height of obstruction {i}? "))
        obstructions_list.append(area(ob_width, ob_height))
        i += 1

    print(obstructions_list)
    area_obstructed = sum(obstructions_list)
    return area_obstructed


def size_breakdown(total_paint_needed):
    rounded_value = round(total_paint_needed)
    print(rounded_value, 1)


wall_count = int(input("How many walls would you like to paint? "))

paint_needed_list = []
colour_needed = []

j = 1

while j <= wall_count:
    print(f"-----WALL {j}-----")
    coating = int(input(f"How many times would you like to coat wall {j}? "))
    width = float(input(f"what is the width of wall {j}? (Meters) "))
    height = float(input(f"What is the height of wall {j}? (Meters) "))
    obstructions = int(input("how many obstructions e.g Windows/Doors/Sockets are present on the wall? "))
    desired_colour()

    total_area_obstructed = wall_obstructions(obstructions)

    print(f"The surface area of the wall is {area(width, height)} m^2")
    print(f"The total area obstructed is {total_area_obstructed} m^2")

    total_area = area(width, height) - total_area_obstructed
    paint_needed_per_coat = total_area / 6
    paint_needed = paint_needed_per_coat * coating

    print(f"The total area to cover is {total_area} m^2")
    print(f"To cover this area you will need {paint_needed_per_coat} litres of paint per coating")
    print(f"As you would like to coat the wall {coating} time(s), you will need {paint_needed} litres of paint")

    paint_needed_list.append(paint_needed)
    j += 1
    #print("You will need " + str(area(width, height) / 6.5) + " litres of paint per coating")

print(paint_needed_list)
print(colour_needed)

