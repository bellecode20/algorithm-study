def solution(orders, course):
    ''' 가장 단순한 방법 먼저
    모든 경우의 수를 다 세어보기
    orders의 크기가 20이고, order의 크기는 10이므로
    20 * 1024 = 2만 = 충분히 작다.
    그럼 전부 다 세면 된다.
    
    1. 모든 조합이 몇 번씩 사용되었는지 세어보기
    2. 조합 내에서 필요한 길이마다 최대 사용 횟수 세어보기
    3. 최대 사용된 조합을 모두 answer에 넣기
    4. answer 정렬 후 출력하기
    '''
    count = {}
    mx_count = {}
    for order in orders:
        for i in range(1<<len(order)):
            S = tuple(sorted({order[j] for j in range(len(order)) if (1<<j)&i}))
            if S not in count:
                count[S] = 0
            count[S] += 1
            if len(S) not in mx_count:
                mx_count[len(S)] = 2
            mx_count[len(S)] = max(mx_count[len(S)],count[S])
    
    answer = [''.join(i) for i in count if len(i) in course and count[i] == mx_count[len(i)]]
    return sorted(answer)
