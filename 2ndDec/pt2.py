# Opening file
data = open('2ndDec\input.txt', 'r')

values = []
round_score = 0

for line in data:

    them = line[0]
    result = line[2]

    if them == "A":
        # rock
        if result == "X":
            # must lose (0 pts), play scissors (3 pts)
            round_score = 3
        elif result == "Y":
            # must draw (3 pts), play rock (1 pt)
            round_score = 4
        elif result == "Z":
            # must win (6 pts), play paper (2 pts)
            round_score = 8

    elif them == "B":
        # paper
        if result == "X":
            # must lose (0 pts), play rock (1 pt)
            round_score = 1
        elif result == "Y":
            # must draw (3 pts), play paper (2 pts)
            round_score = 5
        elif result == "Z":
            # must win (6 pts), play scissors (3 pts)
            round_score = 9
    
    elif them == "C":
        # scissors
        if result == "X":
            # must lose (0 pts), play paper (2 pts)
            round_score = 2
        elif result == "Y":
            # must draw (3 pts), play scissors (3 pts)
            round_score = 6
        elif result == "Z":
            # must win (6 pts), play rock (1 pt)
            round_score = 7

    values.append(round_score)

print(f'Round Scores = {values}')

total_score = 0
for i in values:
    total_score += i

print(f'Total score = {str(total_score)}')