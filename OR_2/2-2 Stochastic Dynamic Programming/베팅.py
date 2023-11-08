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
print(betting_game(stage=5, win_prob=1/3, loss_prob=2/3 , goal_budget=5)[:-1])

"""
출력값:

행: 보유한 코인 개수
열: 베팅하는 코인개수 
값: 최적화된 승률 

즉, 자신이 i개의 코인을 가지고 j개의 코인을 베팅한다면 i+1번째 행의 j+1번째 열을 보면 됩니다. 

1번째 행과 1번째 열은 각각 보유코인이 0개, 베팅코인이 0개임을 의미합니다. 

[[[0.    0.    0.    0.    0.    0.   ]
  [0.062 0.062 0.    0.    0.    0.   ]
  [0.185 0.161 0.185 0.    0.    0.   ]
  [0.358 0.308 0.375 0.333 0.    0.   ]
  [0.555 0.572 0.457 0.375 0.333 0.   ]
  [1.    0.703 0.572 0.457 0.375 0.333]]

 [[0.    0.    0.    0.    0.    0.   ]
  [0.037 0.062 0.    0.    0.    0.   ]
  [0.185 0.136 0.185 0.    0.    0.   ]
  [0.333 0.308 0.358 0.333 0.    0.   ]
  [0.555 0.555 0.457 0.358 0.333 0.   ]
  [1.    0.703 0.555 0.457 0.358 0.333]]

 [[0.    0.    0.    0.    0.    0.   ]
  [0.    0.037 0.    0.    0.    0.   ]
  [0.111 0.111 0.185 0.    0.    0.   ]
  [0.333 0.259 0.333 0.333 0.    0.   ]
  [0.555 0.555 0.407 0.333 0.333 0.   ]
  [1.    0.703 0.555 0.407 0.333 0.333]]

 [[0.    0.    0.    0.    0.    0.   ]
  [0.    0.    0.    0.    0.    0.   ]
  [0.    0.111 0.111 0.    0.    0.   ]
  [0.333 0.111 0.333 0.333 0.    0.   ]
  [0.333 0.555 0.333 0.333 0.333 0.   ]
  [1.    0.555 0.555 0.333 0.333 0.333]]

 [[0.    0.    0.    0.    0.    0.   ]
  [0.    0.    0.    0.    0.    0.   ]
  [0.    0.    0.    0.    0.    0.   ]
  [0.    0.    0.333 0.333 0.    0.   ]
  [0.    0.333 0.333 0.333 0.333 0.   ]
  [1.    0.333 0.333 0.333 0.333 0.333]]]
"""