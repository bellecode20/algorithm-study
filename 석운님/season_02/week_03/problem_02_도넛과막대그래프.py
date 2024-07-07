from collections import defaultdict, deque

def solution(edges):
    answer = []
    """
    나가는 edge가 2개 이상이고 들어오는 edge가 없으면 생성한 정점
    나가는 edge가 2개에다가 그 2개의 edge를 따라가다 둘 다 자신이 나오면 8자
    나가는 edge가 1개이고 그 edge를 따라가는데 중복되는 노드가 없으면 막대
    나가는 edge가 1개이고 그 edge를 따라가다 자신이 나오면 도넛
    """
    incoming, outgoing = defaultdict(int), defaultdict(int)
    node_edges = defaultdict(list)
    nodes = set()
    for e in edges:
        a, b = e[0], e[1]
        incoming[b] += 1
        outgoing[a] += 1
        node_edges[a].append(b)
        nodes.add(a)
        nodes.add(b)
    
    # 생성한 정점 찾기
    for node in nodes:
        if outgoing[node] >= 2 and incoming[node] == 0:
            answer.append(node)
            outgoing[node] = 0
            for a in node_edges[node]:
                incoming[a] -= 1
            break
    nodes.remove(answer[0])

    donut = 0
    bar = 0
    eight = 0

    # 8자형 찾기
    tmp = []
    for node in nodes:
        if outgoing[node] == 2 and incoming[node] == 2:
            visited = deque([node])
            a, b = node_edges[node][0], node_edges[node][1]
            while a != node:
                visited.append(a)
                a = node_edges[a][0]
            while b != node:
                visited.append(b)
                b = node_edges[b][0]
            tmp.append(visited)
            eight += 1
    for t in tmp:
        for v in t:
            nodes.remove(v)

    # 막대 찾기
    tmp = []
    for node in nodes:
        if incoming[node] == 0:
            visited = deque([node])
            a = node
            while len(node_edges[a]) > 0:
                a = node_edges[a][0]
                visited.append(a)
            tmp.append(visited)
            bar += 1
    for t in tmp:
        for v in t:
            nodes.remove(v)

    # 도넛형 찾기
    tmp = []
    while nodes:
        node = nodes.pop()
        visited = deque([])
        a = node_edges[node][0]
        while a != node:
            visited.append(a)
            a = node_edges[a][0]
        while visited:
            v = visited.pop()
            nodes.remove(v)
        donut += 1
    # # print(donut)
    # # print(bar)
    # # print(eight)
    answer.append(donut)
    answer.append(bar)
    answer.append(eight)
            
    
    return answer