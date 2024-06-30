import itertools
from collections import defaultdict

def solution(orders, course):
    answer = []
    course_dict = defaultdict(int)
    
    # 각 주문에 대해 가능한 조합을 생성하고 개수를 기록
    for order in orders:
        for course_num in course:
            if len(order) >= course_num:
                for combi in itertools.combinations(order, course_num):
                    sorted_combi = "".join(sorted(combi))  # 조합을 정렬하여 문자열로 변환
                    course_dict[sorted_combi] += 1
    
    # 각 코스 길이에 대해 가장 많이 주문된 조합을 찾기
    for course_num in course:
        max_count = 2
        most_ordered_combis = []
        for combi, count in course_dict.items():
            if len(combi) == course_num:
                if count > max_count:
                    max_count = count
                    most_ordered_combis = [combi]
                elif count == max_count:
                    most_ordered_combis.append(combi)
        
        answer.extend(most_ordered_combis)
    
    # 최종 답안 정렬
    return sorted(answer)
