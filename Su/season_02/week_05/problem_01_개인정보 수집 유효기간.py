from collections import defaultdict
def solution(today, terms, privacies):
    answer = []
    # 개인정보 n개
    # 유효기간 지나기 전까지 보관 가능
    # 2021.05.02 => 28*12*2021 + 28*5 + 2 일
    #
    # 예시
    # 2021.05.02(privacies)를 일자로 변환한다. 28*12*2021 + 28*5 + 2 일
    # 6달(유효기간)을 일자로 변환한다. 28 * 6 일 = 168일. 
    # 2022.05.19(오늘 날짜)를 일자로 변환한다. 28*12*2022 + 28*5 + 19 일
    # 유효기간 이내인지 체크한다.
    
    deadline_dict = defaultdict(int)
    DAY = 28
    
    def get_converted(info):
        Y, M, D = map(int, info.split("."))
        new_date = (Y * 12 * DAY) + (M * DAY) + D
        return new_date
    
    
    for term in terms:
        name, deadline = term.split(" ")
        deadline_dict[name] = int(deadline) * DAY
        

    new_today = get_converted(today)
    for idx, privacy in enumerate(privacies):
        info, name = privacy.split(" ")
        gap = new_today - get_converted(info)
        if deadline_dict[name] <= gap:
            answer.append(idx + 1)
            
    return answer
