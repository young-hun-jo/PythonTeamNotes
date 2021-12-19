# 아래의 함수를 활용하려면 방향 리스트 dx, dy를 정의할 때, 상/하 , 좌/우를 번갈아가면서 정의해야 함!
# ex) 상,좌,하,우 or 좌,상,우,하 or 하,좌,상,우 , ....
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
