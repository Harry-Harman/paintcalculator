import math

class Wall:
    def __init__(self, coating, width, height, obstructed_area, colour):
        self.coating = coating
        self.width = width
        self.height = height
        self.obstructed_area = obstructed_area
        self.colour = colour


class Paint:
    def __init__(self, brand, p10, p5, p2_5, p1):
        self.brand = brand
        self.price10 = p10
        self.price5 = p5
        self.price2_5 = p2_5
        self.price1 = p1


def area(w, h):
    return w * h


def desired_colour():
    colour = (input("What colour of paint would you like to use on this wall? "))
    colour_needed.append(colour.upper())
    return colour


def wall_obstructions(obst):
    i = 1
    obstructions_list = []
    while i <= obst:
        ob_width = float(input(f"What is the width of obstruction {i}? "))
        ob_height = float(input(f"What is the height of obstruction {i}? "))
        obstructions_list.append(area(ob_width, ob_height))
        i += 1

    #print(obstructions_list)
    area_obstructed = sum(obstructions_list)
    return area_obstructed


def size_breakdown(total_paint_needed):
    litres_left = float(total_paint_needed)
    cans_10 = 0.0
    cans_5 = 0.0
    cans_2_5 = 0.0
    cans_1 = 0.0
    if litres_left >= 10:
        cans_10 = litres_left // 10
        litres_left = litres_left % 10
    if litres_left >= 5 and litres_left < 10:
        cans_5 = litres_left // 5
        litres_left = litres_left % 5
    if litres_left >= 2.5 and litres_left < 5:
        cans_2_5 = litres_left // 2.5
        litres_left = litres_left % 2.5
    if litres_left > 2 and litres_left < 2.5:
        cans_2_5 = cans_2_5 + 1
    if litres_left <= 2:
        cans_1 = litres_left // 1
        litres_left = litres_left % 1
    if litres_left > 0:
        cans_1 += 1

    brand_prices = pricing()
    print(f"To paint this wall you will need:")
    print(f"10L Cans: {cans_10} - Price: {brand_prices.price10 * cans_10}")
    print(f"5L Cans: {cans_5} - Price: {brand_prices.price5 * cans_5}")
    print(f"2.5L Cans: {cans_2_5} - Price: {brand_prices.price2_5 * cans_2_5}")
    print(f"1L Cans: {cans_1} - Price: {brand_prices.price1 * cans_1}")

    total_cost = (brand_prices.price10 * cans_10) + (brand_prices.price5 * cans_5) + (brand_prices.price2_5 * cans_2_5) + (brand_prices.price1 * cans_1)
    print(f"This brings the total cost of this wall to: £{total_cost}")
    log_branding = f"Brand: {brand_prices.brand} \n Buckets: \n 10L: {cans_10} \n 5L: {cans_5} \n 2.5L: {cans_2_5} \n 1L: {cans_1} \n Total cost: {total_cost}"
    log_data(log_file, j, log_branding)



def pricing():
    wickes = ["wickes", 6, 15, 25, 35]
    dulux = ["dulux", 20, 35, 60, 100]
    crown = ["crown", 10, 18, 25, 40]
    brand = (str(input("What brand of paint would you like to use? Wickes(Default)/Dulux/Crown ")))
    brand = brand.upper()
    match brand:
        case "CROWN":
            paint_pricing = Paint(wickes[0], wickes[4], wickes[3], wickes[2], wickes[1])
            return paint_pricing
        case "DULUX":
            paint_pricing = Paint(dulux[0], dulux[4], dulux[3], dulux[2], dulux[1])
            return paint_pricing
        case _:
            paint_pricing = Paint(crown[0], crown[4], crown[3], crown[2], crown[1])
            return paint_pricing


def log_data(log_name, x, log_branding):

    wall_data = f"\n ---Wall data--- \n Wall {x}:\n Dimensions: {wall_info.width} x {wall_info.height} \n Coatings: {wall_info.coating} \n Colour: {wall_info.colour} \n"
    append_file = open(log_name + ".txt", 'a')
    append_file.write(wall_data + log_branding)
    append_file.close()


log_file = str(input("Your data will be logged. Please select a name for your log file"))
wall_count = int(input("How many walls would you like to paint? "))

paint_needed_list = []
colour_needed = []

j = 1

while j <= wall_count:
    print(f"-----WALL {j}-----")
    coating = int(input(f"How many times would you like to coat wall {j}? "))
    width = float(input(f"what is the width of wall {j}? (Meters) "))
    height = float(input(f"What is the height of wall {j}? (Meters) "))
    colour = desired_colour()
    obstructions = int(input("How many obstructions e.g Windows/Doors/Sockets are present on the wall? "))


    total_area_obstructed = wall_obstructions(obstructions)

    wall_info = Wall(coating, width, height, total_area_obstructed, colour)

    total_area = area(width, height) - total_area_obstructed
    paint_needed_per_coat = total_area / 6
    paint_needed = paint_needed_per_coat * coating


    print(f"The surface area of the wall is {area(width, height)} m^2")
    print(f"The total area obstructed is {total_area_obstructed} m^2")


    print(f"The total area to cover is {total_area} m^2")
    print(f"To cover this area you will need {paint_needed_per_coat} litres of paint per coating")
    print(f"As you would like to coat the wall {coating} time(s), you will need {paint_needed} litres of paint")

    paint_needed_list.append(paint_needed)
    print(size_breakdown(paint_needed))

    j += 1


#print(paint_needed_list)
#print(colour_needed)


