# 먄약에 첫 방향이 동쪽을 바라보고 있다고 주어짐
# 동 - 남 - 서 - 북 <-(왼) 동 (오)-> 남 - 서 - 북
# 동 -> 남 -> 서 -> 북(오른쪽) / 동 -> 북 -> 서 -> 남(왼쪽) => 이를 일직선 상에 세운다고 생각
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0   # 처음엔 동쪽 방향을 보고 있음

def turn_direction(direction, c):
    if c == 'left':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


left_direction = turn_direction(direction, 'left')
right_direction = turn_direction(direction, 'right')
print('Left:', left_direction)    # 3(북)
print('Right:', right_direction)  # 1(남)
