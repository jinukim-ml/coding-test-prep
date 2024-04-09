'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/178871
Type: Simulation
'''
def solution(players, callings):
    ranking_name = {}
    ranking_num = {}
    for i in range(len(players)):
        ranking_name[players[i]] = i+1
        ranking_num[i+1] = players[i]
    
    for winner in callings:
        rank = ranking_name[winner]
        loser = ranking_num[rank-1]

        # Position swap
        ranking_num[rank-1] = winner
        ranking_num[rank] = loser
        
        ranking_name[winner] = rank-1
        ranking_name[loser] = rank

    return list(ranking_num.values())

def solution2(players, callings):
    ranking = {}
    for i in range(len(players)):
        ranking[players[i]] = i
    
    for call in callings:
        idx = ranking[call]

        ranking[players[idx]] -= 1
        ranking[players[idx-1]] += 1
        players[idx], players[idx-1] = players[idx-1], players[idx]
    
    return players