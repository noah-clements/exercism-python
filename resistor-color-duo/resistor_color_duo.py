RESISTOR_COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def value(colors):
    if len(colors) < 2:
        raise ValueError("Need two colors")
    return int(str(RESISTOR_COLORS.index(colors[0])) + str(RESISTOR_COLORS.index(colors[1])))


