# Opening file
data = open('1st Dec\input.txt', 'r')

# variables to keep count
elf_calories = 0
elf_most = 0
values = []

for line in data:
    # check if end of elf
    
    if line == "\n":
        
        values.append(int(elf_calories))
        # check if elf has most calories
        if elf_calories > elf_most:
            # set new 'most'
            elf_most = elf_calories
        
        elf_calories = 0
    
    else:
        elf_calories += int(line)

print(f'Cals per Elf = {str(values)}')
print(f'Data type = {type(values)}')
print(f'Most cals = {str(elf_most)}')

# function lifted from https://www.geeksforgeeks.org/python-program-to-find-n-largest-elements-from-a-list/
# comments in here are to rationalise to myself that I know what it's actualy doing :-)
def Nmaxelements(list1, N):
    final_list = []
 
    for i in range(0, N):
        max1 = 0
        
        # iterate through list1 (values list)
        for j in range(len(list1)):    
            # checking if the value is greater than the current maximum
            if list1[j] > max1:
                # if so set max1 to new value
                max1 = list1[j]
        #remove the max from the list
        list1.remove(max1)
        # add the max value to the final list
        final_list.append(max1)
         
    return final_list

elf_top3 = Nmaxelements(values, 3)
elf_top3_total = 0

for x in elf_top3:
    elf_top3_total += x

print(f'Top 3 Elves calorie count = {str(elf_top3)}')
print(f'Top 3 Elves, total calorie count = {str(elf_top3_total)}')

data.close()