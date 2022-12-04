# Opening file
data = open('3rdDec\input.txt', 'r')

total = 0

lookup = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

# func - split string and compare for common chars
def split_compare(string):

    str1, str2 = string[:len(string)//2], string[len(string)//2:]
    return ''.join(set(str1).intersection(str2))

def get_value(char):

    cap_check = char.isupper()
    # print(f'Is uppercase?: {str(cap_check)}')
    charlower = char.lower()

    value = lookup[charlower]
    # print(f'Lookup value: {str(value)}')
    if cap_check == True:
        value += 26
    
    return value

for line in data:

    letter = split_compare(line)
    total += get_value(letter)

print(f'Final total = {str(total)}')
