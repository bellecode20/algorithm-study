def solution(friends, gifts):
    answer = 0
    n = len(friends)
    d = {}
    ans = {}
    arr = [[0 for _ in range(n)] for _ in range(n)]
    record = [0 for _ in range(n)]
    
    # 각 friends의 인덱스와 
    for i, f in enumerate(friends):
        d[f] = i # 각자를 인덱스로 dict에 저장
        ans[i] = 0 
        
    # 선물 주고받은 횟수 저장
    for g in gifts:
        a = g.split(" ")
        arr[d[a[0]]][d[a[1]]] += 1
    
    # 선물 지수를 계산
    for i in range(n):
        give, receive = sum(arr[i]), sum([a[i] for a in arr])
        record[i] = give - receive
        
    
    def comb():
        tmp = []
        def dfs(aa, k):
            if len(aa) == 2:
                tmp.append(aa[:])
                return
            for i in range(k, n):
                dfs(aa + [i], i + 1)
        dfs([], 0)
        return tmp
    
    c = comb()
    for i in range(len(c)):
        a, b = c[i][0], c[i][1]
        if arr[a][b] > arr[b][a]:
            ans[a] += 1
        elif arr[a][b] < arr[b][a]:
            ans[b] += 1
        else:
            if record[a] > record[b]:
                ans[a] += 1
            elif record[a] < record[b]:
                ans[b] += 1
                
    return max(ans.values())