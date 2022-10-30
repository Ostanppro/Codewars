def direction(facing, turn):
    D = {'N':0, 'NE':45, 'E':90, 'SE':135, 'S':180, 'SW':225, 'W':270, 'NW':315}
    F = {0:'N', 45:'NE', 90:'E', 135:'SE', 180:'S', 225:'SW', 270:'W', 315:'NW'}

    y = D[facing] + turn 

    while y >= 360:
        y = y - 360
    
    while y < 0:
        y = y + 360

    return F[y]