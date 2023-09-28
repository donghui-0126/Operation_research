import numpy as np

"""
n_stage 만큼을 베팅 횟수를 통해서 win_prob의 이길확률과 loss_prob의 질 확률을 가진 게임을 통해 goal_budget에 도달할 확률

"""


def betting_game(stage, win_prob, loss_prob, goal_budget):
    mat = np.zeros([stage+1, goal_budget+1, goal_budget+1])
    mat[stage][goal_budget] = 1
    # i: 2->1->0
    for n_stage in reversed(range(stage)):
        for budget in range(goal_budget+1):
            for betting in range(budget+1):            
                win = win_prob * max(mat[n_stage+1][min(budget+betting, goal_budget)]) # 이긴 경우에 
                loss = loss_prob * max(mat[n_stage+1][max(budget-betting, 0)]) # 진 경우에
                mat[n_stage][budget][betting] = round(win+loss,3)
    
    
    return mat

# mat = [(x+1)번째 베팅][y개의 칩을 보유][z개의 칩 베팅]

np.set_printoptions(threshold=np.inf, linewidth=np.inf)
print(betting_game(stage=10, win_prob=0.45, loss_prob=0.55 , goal_budget=10))