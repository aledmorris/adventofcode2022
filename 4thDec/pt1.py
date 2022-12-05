# Opening file
data = open('4thDec\input.txt', 'r')

# convert section assignment to a string
def to_string(x,y):
    string = ''
    for i in range(int(x),int(y)+1):
        string += str(i).zfill(2)+","
    return string


def split_section(section):
    #splits section into the two number values
    coords = section.split("-")
    cordX = coords[0]
    cordY = coords[1]

    return cordX,cordY


def split_line(line):
    # split the line by comma
    sections = line.split(",")
    section1 = sections[0]
    section2 = sections[1]

    xcoords1,ycoords1 = split_section(section1)
    xcoords2,ycoords2 = split_section(section2)

    elf1 = to_string(xcoords1,ycoords1)
    elf2 = to_string(xcoords2,ycoords2)

    return elf1,elf2

total = 0

for line in data:
    #print(f'line = {line}')
    elf1,elf2 = split_line(line)
    overlap = False
    if elf1 in elf2:
        overlap = True
    if elf2 in elf1:
        overlap = True
    if overlap == True:
        total +=1

print(f'Total = {total}')


