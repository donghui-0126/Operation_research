# DP 코드 구현
# 1주차 PPT에 존재하는 다른 길찾기 문제입니다. 

# 행렬 출력함수
def print_matrix(mat):
    for vector in mat:
        print(vector)
    return 


# 행렬에 값을 삽입하는 함수
def insert_mat(mat, start, end, cost):
    mat[start][end] = cost
    return mat


# 행렬 초기화 함수
def init_mat(vector, node_num):
    mat = [[-1 for x in range(node_num)] for xx in range(node_num)]
    for elem in vector:
        start, end, cost = elem[0], elem[1], elem[2]
        insert_mat(mat, start, end, cost)
    return mat


"""
시작지점과 끝지점을 잇는 네트워크의 비용을 나타낸 벡터입니다. 
[시작노드, 도착노드, 비용] 순으로 저장됩니다.
"""
start_end_cost_vector = [
                        [0, 1, 6],[0, 2 ,3],
                        [1, 3, 4],[1, 4, 2],
                        [2, 4, 4],[2, 5, 2],
                        [3, 6, 5],[3, 7, 2],
                        [4, 7, 3],[4, 8, 3],
                        [5, 8, 4],[5, 9, 6],
                        [6, 10, 6],
                        [7, 10, 9],[7, 11, 2],
                        [8, 11, 5],[8, 12, 3],
                        [9, 12, 3],
                        [10, 13, 3],
                        [11,13, 8], [11,14, 7],
                        [12,14,7],
                        [13,15,4],
                        [14,15,6],
                        [15,15,0]
                        ]
                         
matrix = init_mat(start_end_cost_vector, node_num=16)


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
    
cost = solution(matrix, 16)

print("complete optimization!")
print("각 노드에서 end point까지 가는데 드는 비용:", cost)

"""
출력값:
optimizing process... [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 0]
optimizing process... [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 6, 0]
optimizing process... [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 4, 6, 0]
optimizing process... [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 13, 4, 6, 0]
optimizing process... [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 12, 13, 4, 6, 0]
optimizing process... [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 7, 12, 13, 4, 6, 0]
optimizing process... [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 16, 7, 12, 13, 4, 6, 0]
optimizing process... [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 16, 16, 7, 12, 13, 4, 6, 0]
optimizing process... [10000, 10000, 10000, 10000, 10000, 10000, 10000, 14, 16, 16, 7, 12, 13, 4, 6, 0]
optimizing process... [10000, 10000, 10000, 10000, 10000, 10000, 13, 14, 16, 16, 7, 12, 13, 4, 6, 0]
optimizing process... [10000, 10000, 10000, 10000, 10000, 20, 13, 14, 16, 16, 7, 12, 13, 4, 6, 0]
optimizing process... [10000, 10000, 10000, 10000, 17, 20, 13, 14, 16, 16, 7, 12, 13, 4, 6, 0]
optimizing process... [10000, 10000, 10000, 16, 17, 20, 13, 14, 16, 16, 7, 12, 13, 4, 6, 0]
optimizing process... [10000, 10000, 21, 16, 17, 20, 13, 14, 16, 16, 7, 12, 13, 4, 6, 0]
optimizing process... [10000, 19, 21, 16, 17, 20, 13, 14, 16, 16, 7, 12, 13, 4, 6, 0]
optimizing process... [24, 19, 21, 16, 17, 20, 13, 14, 16, 16, 7, 12, 13, 4, 6, 0]


complete optimization!
각 노드에서 end point까지 가는데 드는 비용: [24, 19, 21, 16, 17, 20, 13, 14, 16, 16, 7, 12, 13, 4, 6, 0]
"""