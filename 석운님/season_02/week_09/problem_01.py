# https://school.programmers.co.kr/learn/courses/15009/lessons/121687?language=python3

def solution(command):
    dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]
    direction = 0
    curx, cury = 0, 0
    
    command = list(command)
    for c in command:
        if c == "R":
            direction += 1
            if direction >= 4: 
                direction = 0
        if c == "L":
            direction -= 1
            if direction < 0: 
                direction = 3
        if c == "G":
            curx, cury = curx + dc[direction], cury + dr[direction]
        if c == "B":
            curx, cury = curx - dc[direction], cury - dr[direction]
        
    return [curx, cury]