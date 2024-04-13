'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/172927
Type: Exhaustive search (at least I solve this way)
'''
def search(pickaxe_dict:dict, minerals:list, picks:list, used_picks:list):
    costs = []
    if picks == used_picks:
        return 0
    
    for pick in range(3):
        if picks[pick] == used_picks[pick]:
            continue
        
        used_picks[pick] += 1
        cost = 0

        for j in range(5):
            try:
                cost += pickaxe_dict[pick][minerals[j]]
            except:
                break
        if len(minerals) > 5:
            cost += search(pickaxe_dict, minerals[5:], picks, used_picks)
            used_picks[pick] -= 1
            costs.append(cost)
        else:
            used_picks[pick] -= 1
            costs.append(cost)
            continue
        
    return min(costs)

def solution(picks, minerals):
    answer = []
    used_picks = [0,0,0]

    diamond_pickaxe = {'diamond': 1, 'iron': 1, 'stone': 1}
    iron_pickaxe = {'diamond': 5, 'iron': 1, 'stone': 1}
    stone_pickaxe = {'diamond': 25, 'iron': 5, 'stone': 1}
    pickaxe_dict = [diamond_pickaxe, iron_pickaxe, stone_pickaxe]

    # See 5 ores and use pickaxe to minimize value
    for i in range(3):
        if picks[i] == 0:
            continue
        # choose a pickaxe & add cost accordingly
        used_picks[i] += 1

        cost = 0
        for j in range(5):
            cost += pickaxe_dict[i][minerals[j]]
        
        cost += search(pickaxe_dict, minerals[5:], picks, used_picks)
        
        used_picks[i] -= 1
        
        answer.append(cost)
    
    return min(answer)