# DP 코드 구현
"""
A -> J 까지 10개의 노드가 있음.

이러면 10 x 10 2차원 배열로 각 노드간의 거리를 나타냄.

ex) matrix[0][1]: 0번 노드에서 1번노드의 거리
ex) matrix[0][9] = -1 (만약에 이어지지 않은 노드 이면 -1로 초기화 해줌)
"""

def print_matrix(mat):
    for vector in mat:
        print(vector)
    return 

def insert_mat(mat, start, end, cost):
    mat[start][end] = cost
    return mat

def init_mat(mat, vector):
    for elem in vector:
        start, end, cost = elem[0], elem[1], elem[2]
        insert_mat(mat, start, end, cost)
    return mat

start_end_cost_vector = [
                        [0, 1, 2    ],
                        [0, 2 ,4],
                        [0, 3, 3],
                        [1, 4, 7],
                        [1, 5, 4],
                        [1, 6, 6],
                        [2, 4, 3],
                        [2, 5, 2],
                        [2, 6, 4],
                        [3, 4, 4],
                        [3, 5, 1],
                        [3, 6, 5],
                        [4, 7, 1],
                        [4, 8, 4],
                        [5, 7, 6],
                        [5, 8, 3],
                        [6, 7, 3],
                        [6, 8, 3],
                        [7, 9, 3],
                        [8, 9, 4],
                        [9, 9, 0]
                        ]
                         
matrix = [[-1 for x in range(10)] for xx in range(10)]

matrix = init_mat(matrix, start_end_cost_vector)


# print_matrix(matrix)

def solution(matrix, node_num):
    # 비용을 저장할 list 인 cost 선언
    # minimize 문제이기 때문에 cost의 값을 큰 숫자로 초기화
    # end to end의 cost는 0으로 초기화
    cost = [10000 for x in range(node_num)]    
    cost[node_num-1] = 0
    
    for start in reversed(range(node_num)):
        for end in range(node_num):
            # minimize 문제이기 때문에 더 작은 값으로 업데이트
            if (matrix[start][end]>0) and (cost[start] > matrix[start][end]+cost[end]):
                cost[start] = matrix[start][end] + cost[end]
        print("optimizing process...",cost)
    print("\n")
    return cost
    
cost = solution(matrix, 10)

print("complete optimization!")
print("각 노드에서 end point까지 가는데 드는 비용:", cost)