# check for repeating chars in a string
def check_marker(buffer):
    for char in buffer:
        if buffer.count(char) > 1:
            return True
    return False
# find a marker
def find_marker(datastream,x):
    i = 0
    j = x
    repeat = True
    while repeat:
        check = check_marker(datastream[i:j])
        if check:
            i+=1
            j+=1
        else:
            print(f'Marker = {datastream[i:j]}, Answer = {j}')
            repeat = False

#grab data as a string
data = open('6thDec\input.txt', 'r')
datastream = ''
for line in data:
    datastream = line

print(f'Pt 1:')
find_marker(datastream,4)
print(f'Pt 1:')
find_marker(datastream,14)