# Opening file
data = open('2ndDec\input.txt', 'r')

values = []
round_score = 0

for line in data:
        
    them = line[0]
    me = line[2]
      
    # if they chose Rock
    if them == 'A':
        
        if me == 'X':
            # Rock, Draw, 1 for rock,3 for draw
            round_score = 4
        elif me == 'Y':
            # Paper, Win, 2 for paper, 6 for win
            round_score = 8
        elif me == 'Z':
            # Scissors, Loss, 3 for scissors, 0 for loss
            round_score = 3
    
    # if they chose Paper
    elif them == 'B':

        if me == 'X':
            # Rock, Loss, 1 for rock,0 for loss
            round_score = 1
        elif me == 'Y':
            # Paper, Draw, 2 for paper, 3 for draw
            round_score = 5
        elif me == 'Z':
            # Scissors, Win, 3 for scissors, 6 for win
            round_score = 9
    
    # if they chose scissors
    elif them == 'C':
        
        if me == 'X':
            # Rock, Win, 1 for rock, 6 for win
            round_score = 7
        elif me == 'Y':
            # Paper, Loss, 2 for paper, 0 for loss
            round_score = 2
        elif me == 'Z':
            # Scissors, Draw, 3 for scissors, 3 for Draw
            round_score = 6
    
    values.append(round_score)


print(f'Round Scores = {values}')

total_score = 0
for i in values:
    total_score += i

print(f'Total score = {str(total_score)}')