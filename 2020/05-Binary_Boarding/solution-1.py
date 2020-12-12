seats = []

def findrow(row, start, end):
    for direction in row:
        mid = (start+end)//2
        if direction == "F":
            end = mid    
        else:
            start = mid+1
    return start

def findcol(col, start, end):
    for direction in col:
        mid = (start+end)//2
        if direction == "L":
            end = mid
        else:
            start = mid+1
    return end

with open("input") as i_file:
    for line in i_file:
        row = line[:7]
        col = line[7:]
        seats.append([findrow(row, 0, 127), findcol(col, 0, 7)])

seatsID = [(seats[i][0]*8 + seats[i][1]) for i in range(len(seats))]

print(max(seatsID))
