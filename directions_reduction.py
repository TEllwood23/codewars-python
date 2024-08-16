
def dir_reduc(arr):
    ## initialise direction dict recording NORTH/SOUTH AND EAST/WEST
    direct_dict = {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0}
    ## iterate through list, counting directions (positive for North, negative for South; positive for EAST, negative for WEST)
    for x in arr:
        if x == "NORTH":
            direct_dict["NORTH"] += 1
        if x == "SOUTH":
            direct_dict["SOUTH"] -= 1
        if x == "EAST":
            direct_dict["EAST"] += 1
        if x == "WEST":
            direct_dict["WEST"] -= 1

    north_south = direct_dict["NORTH"]+direct_dict["SOUTH"]
    east_west = direct_dict["EAST"]+direct_dict["WEST"]
    print(f"north_south is {north_south}")
    print(f"east_west is {east_west}")
    final_directions = []
    while north_south > 0:
        final_directions.append("NORTH")
        north_south -= 1

    while north_south < 0:
        final_directions.append("SOUTH")
        north_south += 1

    while east_west > 0:
            final_directions.append("EAST")
            east_west -= 1

    while east_west < 0:
            final_directions.append("WEST")
            east_west += 1

    return final_directions
