from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for r in course: # n C r: r개의 
        candidates = []
        for order in orders:
            # 각 주문별로 r개의 조합을 구하고 candidates 배열에 저장
            for comb in combinations(list(order), r):
                candidates.append("".join(sorted(list(comb))))

        # Counter객체로 세트메뉴를 많이 겹치는 순서대로 c_cand에 저장
        c_cand = Counter(candidates).most_common()
        
        # 가장 많이 겹치는 세트메뉴가 정답, 이때 개수가 2개 이상이어야 함
        for i, c in enumerate([a for a in c_cand if a[1] >= 2 and a[1] == c_cand[0][1]]):
            answer.append(c[0])
            
    return sorted(answer)
            
