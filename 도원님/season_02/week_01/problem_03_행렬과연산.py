
def solution(rc, operations):
    R = len(rc)
    C = len(rc[0])
    shift_count = 0 # 0~ R-1 시작행을 나타냄
    
    def rotate(shift_count):
        start_row = (-shift_count)%R
        end_row = start_row-1 # -1~ R-2
        idxs = []
        for i in range(C-1):
            idxs.append((start_row,i))
        for i in range(start_row, start_row+R-1):
            idxs.append((i%R,C-1))
        for i in range(C-1,0,-1):
            idxs.append((end_row,i))
        for i in range(end_row,end_row-R+1,-1):
            idxs.append((i%R,0))
        return idxs
        
    rotate_idxs = [rotate(i) for i in range(R)]
        
    def rot_shif(rot, shif):
        idxs = rotate_idxs[shif]
        rot_idxs = idxs[rot:]+idxs[:rot]
        vals = [rc[r][c] for r,c in idxs]
        for i in range(len(rot_idxs)):
            r,c = rot_idxs[i]
            rc[r][c] = vals[i]
        #rot좌표에 idxs좌표의 값을 넣어야 함
    r_stk = 0 #돌릴 횟수
    for i in operations:
        if i[0] == 'S':
            rot_shif(r_stk, shift_count)
            shift_count += 1
            shift_count%=R
            r_stk = 0
        else:
            r_stk += 1
    rot_shif(r_stk, shift_count)
    
    
    return rc[-shift_count:]+rc[:R-shift_count]