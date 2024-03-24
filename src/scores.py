def scores(player_one, player_two):
    p1 = 0
    p2 = 0
    
    if len(player_one) != len(player_two):
        return 'List length not equal.'
    
    for i in range(len(player_one)):
        if player_one[i] > player_two[i]:
            p1 += 1
        elif player_two[i] > player_one[i]:
            p2 += 1
            
    return f'Player One: {p1} - Player Two: {p2}'

p1 = [2, 8, 6]
p2 = [3, 5, 7]
print(scores(p1, p2))