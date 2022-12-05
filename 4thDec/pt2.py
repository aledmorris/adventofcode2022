# Opening file
data = open('4thDec\input.txt', 'r')

# convert section assignment to a string
def to_list(x,y):
    list = []
    for i in range(int(x),int(y)+1):
        list.append(str(i).zfill(2))
    return list

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

    elf1 = to_list(xcoords1,ycoords1)
    elf2 = to_list(xcoords2,ycoords2)

    return elf1,elf2

total = 0

for line in data:
    #print(f'line = {line}')
    elf1,elf2 = split_line(line)
    overlap = ''.join(set(elf1).intersection(elf2))
    if overlap:
        total += 1

print(f'Total = {total}')


