# 프로젝트 문제 3번
input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]
N = 4

forest = []

def problem3(input):
    bear_size = 2
    honeycomb_count = 0
    time = 0
    bear_x, bear_y = 0, 0
    # 입력 힌트

    # forest 리스트를 input 리스트로 초기화
    forest = [row[:] for row in input]
    
    # 곰의 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0
    print("곰의 초기 위치 x : {0}, y : {1}".format(bear_x, bear_y))

    #여기에서부터 코드를 작성하세요.
    from collections import deque

    def bfs():
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(bear_x, bear_y, 0)])
        visited = [[False] * N for _ in range(N)]
        visited[bear_x][bear_y] = True
        possible_honeycombs = []
        
        while queue:
            x, y, dist = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if forest[nx][ny] <= bear_size:
                        visited[nx][ny] = True
                        if 0 < forest[nx][ny] < bear_size:
                            possible_honeycombs.append((dist + 1, nx, ny))
                        queue.append((nx, ny, dist + 1))
        
        if possible_honeycombs:
            possible_honeycombs.sort()
            return possible_honeycombs[0]
        else:
            return None
    
    while True:
        target = bfs()
        if not target:
            break
        dist, x, y = target
        bear_x, bear_y = x, y
        forest[bear_x][bear_y] = 0
        honeycomb_count += 1
        time += dist
        
        if honeycomb_count == bear_size:
            bear_size += 1
            honeycomb_count = 0

    result = time
    return result

result = problem3(input)

assert result == 14
print("정답입니다.")
