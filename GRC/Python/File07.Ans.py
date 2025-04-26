import string
def game_score(difficulty, team, level):
    score = 0
    difficulties = {
        "easy" : 50, 
        "medium" : 100, 
        "hard" : 200
        }
    
    teams = {
        "solo" : 500, 
        "duo" : 300, 
        "triple" : 200, 
        "squad" : 100
        }
    
    if difficulty in difficulties:
        score += difficulties[difficulty]
    else:
        print("Error: Invalid difficulty")
    if team in teams:
        score += teams[team]
    else:
        print("Error: Invalid Team")
        
    for i in range(level):
        score += 100
    
    return score

difficulty = input("Enter a diffiulty: ").lower().strip()
team = input("Enter a team: ").lower().strip()
levels = int(input("Enter the number of levels: "))
print(game_score( difficulty, team, levels))
    