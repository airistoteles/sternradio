def load(stations_file):
    stations_list = []
    temp1 = []
    temp2 = []
    with open(stations_file, 'r') as stats:
        for line in stats:
            temp1.append(line)

    for line in temp1:
        if line[0] == "#":
            if len(temp2)>0:
                stations_list.append(temp2)
            temp2 = []
        elif line[0:2] != "\n":
            temp2.append(line[:len(line)-1])
    stations_list.append(temp2)

    return stations_list
