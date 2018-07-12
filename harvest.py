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

    print(melon_dict)

make_melon_type_lookup(make_melon_types())

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



