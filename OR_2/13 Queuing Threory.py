"""
M/M/S/K(M/G/SK) 모형을 코딩

이 코드의 목적은 S의 수를 고려해서 기대 이익을 최대화하는 코드입니다. 

Maximize Profit_per_hour: (profit_per_client) x (client_per_hour(in system) - client_exeeding_K - client_no_patient) - (delta_S * cost_S) - (delta_K * cost_K)

parameter:  profit_per_client, mu, lambda, init_S, init_K, limit_waiting_time, 
            P(exit|half_waiting_time), P(exit|quater_waiting_time), P(exit|three_quater_waiting_time),
            delta_S, delta_K
            
optional parameter: Balance

return: optimal Profit per hour, optimal S, optimal K, (sub optimal Profit per hour, sub_optimal S, sub_optimal K, money_recovery_period)[Balance consideration] 

어떤방식으로 최적화 할 것인가.. (결국에 내가 정하지 않은 parameter는 delta_S, delta_K 이 두값만 얻으면 된다.)
그냥 모든 s에 대해서 계산해보면 될 것 같다.(일단은 그렇게 하자) 
두값이 정수기 때문에.. 정수최적화를 해야할듯? (근데 목적함수랑 조건식이 선형식이 아닐듯)
"""

"""
이 다음 프로젝트로는 위 함수를 이용해서 하루동안의 S 수를 최적화해볼 수 있을 것 같다. (시간당 mu lambda가 다를 수 있기 때문에) 
이건... 선형계획법으로 풀어본 기억이 있는데, 다르다. 
왜냐하면 s수에 따라서 profit이 선형이 아니기 때문에.... 


hoxy... 강화학습으로 풀이가능..?
"""