def decode_resistor_colors(bands):
    codes = {"black": 0, "brown": 1, "red": 2, "orange": 3,
        "yellow": 4, "green": 5, "blue": 6, "violet": 7,
        "gray": 8, "white": 9, "gold": 5, "silver": 10}
    
    bands = bands.split()
    
    if len(bands) > 3:
        tol = codes[bands[3]]
    else:
        tol = 20
    
    ohms = (10 * codes[bands[0]] + codes[bands[1]]) * 10 ** codes[bands[2]]
    
    if ohms > 999999:
        ohms = str(ohms / 1000000.0) + "M"
    elif ohms > 999:
        ohms = str(ohms / 1000.0) + "k"
    else:
        ohms = str(ohms)
    
    
    return "%s ohms, %d%%" % (ohms.replace(".0", ""), tol)