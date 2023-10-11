# DP 코드 구현
# 2주차 의료진파견 문제


# 행렬 출력 함수
def print_matrix(mat):
    for vector in mat:
        print(vector)
    return 


# 행렬에 값을 추가해주는 함수
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
1주차와 마찬가지로 문제를 네트워크화 시켰습니다. 
PPT를 참고하시면 네트워크를 찾을 수 있습니다. 

시작지점과 끝지점을 잇는 네트워크의 비용을 나타낸 벡터입니다. 
[시작노드, 도착노드, 비용] 순으로 저장됩니다.
"""
start_end_cost_vector = [
                         [0,1,120],[0,2,105],[0,3,90],[0,4,70],[0,5,45],[0,6,0],
                         [1,7,0],[2,7,20],[2,8,0], [3,7,45], [3,8,20], [3,9,0],
                         [4,7,75],[4,8,45],[4,9,20],[4,10,0],
                         [5,7,110], [5,8,75],[5,9,45],[5,10,20],[5,11,0],
                         [6,7,150],[6,8,110],[6,9,75],[6,10,45],[6,11,20],[6,12,0],
                         [7,13,0], [8,13,50], [9,13,70],[10,13,80],[11,13,100],[12,13,130],
                         [13,13,0]]

# 노드개수
node_num=14

# 행렬 초기화
matrix = init_mat(start_end_cost_vector, node_num=node_num)


"""
보상을 최대화하는 문제기 때문에 1주차 코드와 다릅니다. 
"""
def solution(matrix, node_num):
    # 비용을 저장할 list 인 cost 선언
    # maximize 문제기 때문에 cost의 값을  0으로 초기화
    # end to end의 cost는 0으로 초기화
    cost = [0 for x in range(node_num)]    
    cost[node_num-1] = 0
    
    for start in reversed(range(node_num)):
        for end in range(node_num):
            if (matrix[start][end]>0) and (cost[start] < matrix[start][end]+cost[end]):
                cost[start] = matrix[start][end] + cost[end]
        
        print("optimizing process...",cost)
    print("\n")
    
    
    
    return cost
    
cost = solution(matrix, node_num=node_num)

print("complete optimization!")
print("각 노드에서 출발해서 end point로 가면서 얻는 보상:", cost)

"""
출력값:
optimizing process... [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
optimizing process... [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 130, 0]
optimizing process... [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 130, 0]       
optimizing process... [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 80, 100, 130, 0]      
optimizing process... [0, 0, 0, 0, 0, 0, 0, 0, 0, 70, 80, 100, 130, 0]     
optimizing process... [0, 0, 0, 0, 0, 0, 0, 0, 50, 70, 80, 100, 130, 0]    
optimizing process... [0, 0, 0, 0, 0, 0, 0, 0, 50, 70, 80, 100, 130, 0]    
optimizing process... [0, 0, 0, 0, 0, 0, 160, 0, 50, 70, 80, 100, 130, 0]  
optimizing process... [0, 0, 0, 0, 0, 125, 160, 0, 50, 70, 80, 100, 130, 0]
optimizing process... [0, 0, 0, 0, 95, 125, 160, 0, 50, 70, 80, 100, 130, 0]
optimizing process... [0, 0, 0, 70, 95, 125, 160, 0, 50, 70, 80, 100, 130, 0]
optimizing process... [0, 0, 20, 70, 95, 125, 160, 0, 50, 70, 80, 100, 130, 0]
optimizing process... [0, 0, 20, 70, 95, 125, 160, 0, 50, 70, 80, 100, 130, 0]
optimizing process... [170, 0, 20, 70, 95, 125, 160, 0, 50, 70, 80, 100, 130, 0]


complete optimization!
각 노드에서 출발해서 end point로 가면서 얻는 보상: [170, 0, 20, 70, 95, 125, 160, 0, 50, 70, 80, 100, 130, 0]

즉, 최적화된 보상은 170 입니다. 
"""