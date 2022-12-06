# check for repeating chars in a string
def check_marker(buffer):
    for char in buffer:
        if buffer.count(char) > 1:
            return True
    return False

#grab data as a string
data = open('6thDec\input.txt', 'r')
datastream = ''
for line in data:
    datastream = line

i = 0
j = 14
repeat = True
while repeat:
    check = check_marker(datastream[i:j])
    if check:
        i+=1
        j+=1
    else:
        print(f'Marker = {datastream[i:j]}, Answer = {j}')
        repeat = False