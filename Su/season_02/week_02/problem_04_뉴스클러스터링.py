from collections import defaultdict
def solution(str1, str2): 
    
    obj_1 = defaultdict(int) # str_1 모든 문자열 조각 모음
    obj_2 = defaultdict(int) # str_2의 모든 문자열 조각 모음
    obj_total = defaultdict(int) # str_1과 str_2의 모든 문자열 조각 모음
    
    for i in range(0, len(str1) - 1):
        new_str = str1[i] + str1[i+1] # 두글자씩 자르기
        if not new_str.isalpha(): # 특수문자 있는 경우, 원소로 삼지 않는다.
            continue;
        lower_new_str = new_str.lower()
        obj_1[lower_new_str] += 1
        obj_total[lower_new_str] += 1
    
    for i in range(0, len(str2) - 1):
        new_str = str2[i] + str2[i+1]
        if not new_str.isalpha(): # 특수문자 있는 경우, 원소로 삼지 않는다.
            continue;
        lower_new_str = new_str.lower()
        obj_2[lower_new_str] += 1
        obj_total[lower_new_str] += 1
        

    intersectionCount = 0 
    unionCount = 0
    
    for key in obj_total.keys():
        thisIntersection = min(obj_1[key], obj_2[key]) 
        unionCount += obj_total[key] - thisIntersection # 합집합
        intersectionCount += thisIntersection # 교집합
        
        
    if intersectionCount == 0 and unionCount == 0:
        J = 1 # A와 B가 공집합인 경우
    else:
        J = intersectionCount / unionCount
    
    return int(J * 65536)