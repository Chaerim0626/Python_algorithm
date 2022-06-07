def solution(places):
    answer = []
    for i in range(5):
        places[i]


    return answer
def is_valid_coord(y,x):
    return 0 <= x < 5 and 0 <= y < 5

def dfs(y,x,board):
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny,nx) and board[ny][nx] == 'O'


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))