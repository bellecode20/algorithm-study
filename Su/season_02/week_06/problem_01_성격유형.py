def solution(survey, choices):
    answer = ''
    dict = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0} # 유형마다 점수 기록하기
    
    # 1. [점수 계산]
    #   1-1. 유형마다 점수 dict 생성
    #   1-2. 점수 계산
    #        1, 7 응답 => 3점
    #        2, 6 응답 => 2점
    #        3, 5 응답 => 1점
    # 
    # 2. [유형 결정]
    #   2-1. 점수가 높은 유형 선택
    #   2-2. 점수가 같은 경우, 사전 순

    # 예시: 
    # choices = [5, 3, 2, 7, 5] 
    # survey = ["AN", "CF", "MJ", "RT", "NA"]   
    # survey[i]의 첫 번째 캐릭터는 i+1번 질문의 비동의 관련 선택지(1~3)를 선택하면 받는 성격 유형을 의미합니다.
    # survey[i]의 두 번째 캐릭터는 i+1번 질문의 동의 관련 선택지(5~7)를 선택하면 받는 성격 유형을 의미합니다.

    # [점수 계산 방식]
    # 매우 동의나 매우 비동의 선택지를 선택하면 3점을 얻습니다.
    # 동의나 비동의 선택지를 선택하면 2점을 얻습니다.
    # 약간 동의나 약간 비동의 선택지를 선택하면 1점을 얻습니다.
    for i in range(len(choices)):
        if choices[i] == 4: # "잘 모르겠다" -> 아무도 점수 얻지 않음
            continue
        elif choices[i] > 4: # 5 ~ 7 선택
            dict[survey[i][1]] += choices[i]-4 # 만약 choices[i]가 5인 경우, 5 - 4 = 1점 기록, choices[i]가 6인 경우, 6 - 4 = 2점 기록
        elif choices[i] < 4: # 1 ~ 3 선택
            dict[survey[i][0]] += -choices[i]+4 # 만약 choices[i]가 1인 경우, -1 + 4 = 3점 기록
    
    # 유의: 점수가 같은 경우, 사전 순
    if dict["R"] >= dict["T"]:
        answer += "R" 
    else:
        answer += "T"
    if dict["C"] >= dict["F"]:
        answer += "C"
    else:
        answer += "F"
    if dict["J"] >= dict["M"]:
        answer += "J"
    else:
        answer += "M"
    if dict["A"] >= dict["N"]:
        answer += "A"
    else:
        answer += "N"
    return answer
