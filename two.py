def players_score(player_one, player_two):
    first_score = 0
    second_score = 0
    
    if len(player_one) == len(player_two):
        for i in range(len(player_one)):
            if player_one[i] > player_two[i]:
                first_score += 1
            elif player_one[i] < player_two[i]:
                second_score += 1
    else:
        return f'Error in the length points of players'
    
    return f'P1: {first_score} - P2: {second_score} - {[first_score, second_score]}'


player_one = [2, 5, 5, 9, 6]
player_two = [5, 3, 7, 8, 3]
print(players_score(player_one, player_two))