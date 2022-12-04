from itertools import islice

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
# comparison logic lifted form https://www.geeksforgeeks.org/python-program-find-common-elements-three-lists-using-sets/
def split_compare(string):

    list1 = list(string[0])
    list2 = list(string[1])
    list3 = list(string[2])
    

    # Converting the arrays into sets
    s1 = set(list1)
    s2 = set(list2)
    s3 = set(list3)

    # Calculates intersection of 
    # sets on s1 and s2
    set1 = s1.intersection(s2)         
      
    # Calculates intersection of sets
    # on set1 and s3
    result_set = set1.intersection(s3)
      
    # Converts resulting set to list
    final_list = list(result_set)
    
    return final_list[0]

def get_value(char):

    cap_check = char.isupper()
    charlower = char.lower()
    value = lookup[charlower]
    if cap_check == True:
        value += 26
    
    return value


# Opening file
with open('3rdDec\input.txt', 'r') as infile:
    group = []
    for line in infile:
        group.append(line.strip())
        if len(group) >= 3:
            letter = split_compare(group)
            total += get_value(letter)
            group = []

print(f'Total = {total}')
