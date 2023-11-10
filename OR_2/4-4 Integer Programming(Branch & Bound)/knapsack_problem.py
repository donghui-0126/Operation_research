# https://www.geeksforgeeks.org/branch-and-bound-algorithm/
# 위 링크에서 코드를 카피하고 한글 주석을 새로 달면서 알고리즘을 이해했음. 


from queue import Queue
from functools import cmp_to_key


MAX_WEIGHT = 100

# 냅색 문제를 풀기위해서 새로운 Item 자료구조 생성
class Item:
	def __init__(self, weight, value):
		self.weight = weight
		self.value = value

# 노드 생성
# level: Tree의 깊이
# profit: 효용
# bound: 목적함수의 최적값
# weight: 무게 
class Node:
	def __init__(self, level, profit, bound, weight):
		self.level = level
		self.profit = profit
		self.bound = bound
		self.weight = weight

# 무게당 효용으로 Item을 정렬할 때 사용됨
def compare(a, b):
	r1 = float(a.value) / a.weight
	r2 = float(b.value) / b.weight
	return r1 > r2


# 해당노드의 최적값을 도출
def bound(node, num_item, max_W, item_arr):
	# 노드의 최적해가 불가능한 해라면, 최적값 업데이트를 안하기 위해서 0 반환 
	if node.weight >= max_W:
		return 0

    # 노드의 최적해가 가능해라면, 기존 최적값과 비교
	profitBound = node.profit
	
 	# n 레벨의 노드에서는 n+1 인덱스부터 item을 넣을지 말지 선택
	# item을 무게별 효용을 sorting한 다음 알고리즘에 들어가기 때문에
	# 초기노드의 level이 -1이기 때문에, 조금만 생각해보면 납득 가능함.
	j = node.level + 1
	total_weight = int(node.weight)

	# index를 넘어가지 않는 조건과 제약조건을 넘어가지 않는 선에서 최적화
	while j < num_item and total_weight + int(item_arr[j].weight) <= max_W:
		total_weight += int(item_arr[j].weight)
		profitBound += item_arr[j].value
		j += 1
    
	# 가방에 들어가는 물건을 끝까지 고려하지 못했을 때, 
	# 가능해는 아니지만(max W를 넘어가는 상황) 최적값을 구해준다
	if j < num_item:
		profitBound += int((max_W - total_weight) * item_arr[j].value / item_arr[j].weight)

	return profitBound

# 냅색문제 풀기
def knapsack_solution(max_W, item_arr, num_item):
	item_arr.sort(key=cmp_to_key(compare), reverse=True)
 
	# Queue를 통해서 노드들을 저장함
	q = Queue()
	# 첫번째 Root Node 생성
	u = Node(-1, 0, 0, 0)
	q.put(u)

	# optimal을 0으로 초기화
	maxProfit = 0

	# queue에서 값을 얻고 반환한다.
	while not q.empty():
		u = q.get()


		if u.level == -1:
			v = Node(0, 0, 0, 0)

		# 모든 경우를 고려했으니 아무것도 하지않는다. 
		if u.level == num_item - 1:
			continue
		
		# 다음 Item이 추가되는 새로운 노드를 생성한다.
		v = Node(u.level + 1, u.profit +
				item_arr[u.level + 1].value, 0, u.weight + item_arr[u.level + 1].weight)

		# (가능해 AND 최적값 > 기존최적값) => 최적값 
		if v.weight <= max_W and v.profit > maxProfit:
			maxProfit = v.profit

		# 다음 Item이 추가되는 노드에서 
		# 최적값 bound를 구한다. 
		v.bound = bound(v, num_item, max_W, item_arr)

		# 굳이 조사할 필요가 없는 노드(F(1)에 근거함)를 조사하지 않음.
		# 굳이 queue에 삽입하지 않는다.
		if v.bound > maxProfit:
			q.put(v)

		# 다음 Item이 추가되지 않는 노드를 생성
		v = Node(u.level + 1, u.profit, 0, u.weight)
		# 다음 Item이 추가되지 않는 노드의 bound 계산
		v.bound = bound(v, num_item, max_W, item_arr)
		# 굳이 조사할 필요가 없는 노드(F(1)에 근거함)를 조사하지 않음.
		# 굳이 queue에 삽입하지 않는다. 
		if v.bound > maxProfit:
			q.put(v)

	return maxProfit




# Driver Code
if __name__ == '__main__':
	max_W = 100
	item_arr = [Item(40, 40), Item(50, 60), Item(
		30, 10), Item(10, 10), Item(10, 3),
        Item(40, 20), Item(30, 60)]
	num_item = len(item_arr)

	print('Maximum possible profit =', knapsack_solution(max_W, item_arr, num_item))
