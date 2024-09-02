## 트리

### 문제 1.
아래에 첨부된 make_tree 함수를 실행하여 노드의 개수가 15개인 트리를 생성하고, 두 노드를 입력 받아 노드를 연결하는 간선의 개수를 구하세요.

### 문제 2.
아래에 첨부된 make_complete_binary_tree 함수를 실행하여 노드의 개수가 15개인 완전 이진 트리를 생성하고, 두 노드를 입력 받아 노드를 연결하는 간선의 개수를 구하세요.

### 문제 3.
아래에 첨부된 make_tree 함수를 실행하여 노드의 개수가 15개인 트리를 생성하고, 트리 내에서 가장 긴 단순 경로의 길이를 구하세요.

``` python
import tkinter as tk
import random

# 편의를 위해 부모노드는 무조건 자식노드보다 낮은 번호를 가진다.
def make_tree(n): # 트리의 크기
    P = [-1]+[random.randint(0,i-1) for i in range(1,n)]

    return P

def make_binary_tree(n): # 이진트리 생성 함수
    P = [-1]
    S = [0]
    for i in range(1,n):
        not_filled = [i for i in range(len(P)) if S[i]<2]
        p = random.choice(not_filled)
        P.append(p)
        S[p]+=1
        S.append(0)
    return P

def make_complete_binary_tree(n):
    #return [(i+1)//2-1 for i in range(n)]
    # 이해를 돕기 위해 아래 코드를 사용한다.
    # 더미로 생기는 0번 노드는 무시한다.
    return [i//2 for i in range(n+1)]

def make_picture(tree): # 시각화 함수 
    N = len(tree)
    sons = [ [] for _ in range(N)]
    for i in range(1,N):
        sons[tree[i]].append(i)
        
    depth = [1]
    for i in range(1,N):
        depth.append(depth[tree[i]]+1)

    depth_dic = {i:[] for i in range(1,N+1)}
    stk = [0]
    width = [0]*N
    for cur in stk:
        width[cur] = len(depth_dic[depth[cur]])
        depth_dic[depth[cur]].append(cur)
        for nxt in sons[cur]:
            stk.append(nxt)

    for i in range(N):
        cvs.create_oval( 10+width[i]*50, 10+depth[i]*50, width[i]*50+40,depth[i]*50+40)

    for i in range(1,N):
        cvs.create_line(25+width[i]*50, 25+depth[i]*50, 25+width[tree[i]]*50, 25+depth[tree[i]]*50)
        cvs.create_text(25+width[i]*50, 25+depth[i]*50, text=str(i))
        
root = tk.Tk()
cvs = tk.Canvas(width=800,height=600,bg='white')
cvs.pack()

tree = make_complete_binary_tree(15)
make_picture(tree)
```