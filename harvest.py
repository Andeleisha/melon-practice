############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""
   

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    muskmelon = MelonType("musk", "1998", "green", True, True, "Muskmelon")
    muskmelon.add_pairing("Mint")
    all_melon_types.append(muskmelon)

    casaba = MelonType("cas", "2003", "orange", True, False, "Casaba")
    casaba.add_pairing("Strawberry")
    casaba.add_pairing("Mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren", "1996", "green", True, False, "Crenshaw")
    crenshaw.add_pairing("proscuitto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType("yw", "2013", "yellow", True, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    # print(all_melon_types)
    return all_melon_types

# make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print("{} pairs with".format(melon.name))
        for item in melon.pairings:
            print("- {}".format(item)) 

# print_pairing_info(make_melon_types())

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}
    # Fill in the rest
    for melon in melon_types:
        melon_dict[melon.code] = melon_dict.get(melon.code, melon)

    
    # print(melon_dict)
    return melon_dict

# make_melon_type_lookup(make_melon_types())

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, name, melon_type, shape_rating, color_rating, field, harvested_by):
        self.name = name
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested_by = harvested_by


    def is_sellable(self):
        if self.field != 3 and self.shape_rating > 5 and self.color_rating > 5:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_harvested = []
    # Fill in the rest
    melon_1 = Melon("Melon 1", melon_types["yw"], 8, 7, 2, "Sheila")
    melons_harvested.append(melon_1)
    melon_2 = Melon("Melon 2", melon_types["yw"], 3, 4, 2, "Sheila")
    melons_harvested.append(melon_2)
    melon_3 = Melon("Melon 3", melon_types["yw"], 9, 8, 3, "Sheila")
    melons_harvested.append(melon_3)
    melon_4 = Melon("Melon 4", melon_types["cas"], 10, 6, 35, "Sheila")
    melons_harvested.append(melon_4)
    melon_5 = Melon("Melon 5", melon_types["cren"], 8, 9, 35, "Michael")
    melons_harvested.append(melon_5)
    melon_6 = Melon("Melon 6", melon_types["cren"], 8, 2, 35, "Michael")
    melons_harvested.append(melon_6)
    melon_7 = Melon("Melon 7", melon_types["cren"], 2, 3, 4, "Michael")
    melons_harvested.append(melon_7)
    melon_8 = Melon("Melon 8", melon_types["musk"], 6, 7, 4, "Michael")
    melons_harvested.append(melon_8)
    melon_9 = Melon("Melon 9", melon_types["yw"], 7, 10, 3, "Sheila")
    melons_harvested.append(melon_9)

    # print(melons_harvested)
    return melons_harvested

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 
    for melon in melons:
        melon_name = melon.name
        harvested_by = melon.harvested_by
        field = melon.field
        can_be_sold = melon.is_sellable()
        # print("{} harvested by {} from Field # {}".format(melon_name, harvested_by, field))
        #print(f "{melon_name} harvested by {harvested_by} from Field # {field}")
        print("{} harvested by {} from Field # {} ".format(melon_name, harvested_by, field), end="")
        if can_be_sold :
            print("CAN BE SOLD")
        else:
            print("IS NOT SELLABLE")



# melon_1 = Melon("Melon 1", "yw", 8, 7, 2, "Sheila")
# melon_2 = Melon("Melon 2", "yw", 3, 4, 2, "Sheila")
# melon_3 = Melon("Melon 3", "yw", 9, 8, 3, "Sheila")
# melon_4 = Melon("Melon 4", "cas", 10, 6, 35, "Sheila")
# melon_5 = Melon("Melon 5", "cren", 8, 9, 35, "Michael")
# melon_6 = Melon("Melon 6", "cren", 8, 2, 35, "Michael")
# melon_7 = Melon("Melon 7", "cren", 2, 3, 4, "Michael")
# melon_8 = Melon("Melon 8", "musk", 6, 7, 4, "Michael")
# melon_9 = Melon("Melon 9", "yw", 7, 10, 3, "Sheila")






stuff = make_melon_types()

dictionary = make_melon_type_lookup(stuff)

melons = make_melons(dictionary)

get_sellability_report(melons)

