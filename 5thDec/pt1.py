stacks = {
    1: 'mjcbfrlh',
    2: 'zcd',
    3: 'hjfcngw',
    4: 'pjdmtsb',
    5: 'ncdrj',
    6: 'wldqpjgz',
    7: 'pztfrh',
    8: 'lvmg',
    9: 'cbgpfqrj'
}

def get_move(line):
    parts = line.split(" ")
    payload = parts[1]
    src = parts[3]
    dst = parts[5]
    return int(payload),int(src),int(dst)

def move_payload(load,src,dst):
    # crane grabs crates to move
    crane = stacks[src][-load:]
    enarc = crane[::-1]
    # remove payload from src
    stacks[src] = stacks[src][:-load]
    # add payload to dst
    stacks[dst] += enarc

# Opening file
data = open('5thDec\moves.txt', 'r')

for line in data:
    values = get_move(line)
    move_payload(values[0],values[1],values[2])

print(stacks)
top =''
for str in stacks:
    top += stacks[str][-1:].upper()

print(f'Top of Stacks = {top}')