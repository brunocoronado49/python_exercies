from random import choice

def select_tech(tech):
    pointsJs = 0
    pointsPy = 0

    for i in range(10):
        result = choice(tech)
    
        if result == 'python':
            pointsPy += 1
        else:
            pointsJs += 1
            
    return f'Resultado final: Python {pointsPy} - Javascript {pointsJs}'


techs = ['python', 'js', 'python', 'js', 'python', 'js']
print(select_tech(techs))