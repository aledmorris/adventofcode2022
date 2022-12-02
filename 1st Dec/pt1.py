# Opening file
data = open('1st Dec\input.txt', 'r')

# variables to keep count
elf_calories = 0
elf_most = 0

for line in data:
    #check if end of elf
    if line == "\n":
        # check if elf has most calories
        if elf_calories > elf_most:
            # set new 'most'
            elf_most = elf_calories
        elf_calories = 0
    else:
        elf_calories += int(line)

print(f'Most cals = {str(elf_most)}')
# Closing files
data.close()