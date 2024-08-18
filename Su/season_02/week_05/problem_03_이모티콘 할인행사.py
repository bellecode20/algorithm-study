def solution(users, emoticons):
    answer = [0, 0]
    data = [10, 20, 30, 40]
    discount_combinations = []
    
    # 모든 가능한 이모티콘 할인율 조합을 생성
    def generate_discounts(temp):
        if len(temp) == len(emoticons):
            discount_combinations.append(temp[:])
            return
        for d in data:
            temp.append(d)
            generate_discounts(temp)
            temp.pop()
    
    generate_discounts([])

    # 각 할인율 조합을 평가
    for disc in discount_combinations:
        sum_apply = 0
        sum_price = 0
        
        for user in users:
            min_disc, threshold = user
            total_cost = 0
            
            for i in range(len(emoticons)):
                if disc[i] >= min_disc:
                    total_cost += emoticons[i] * (1 - disc[i] / 100)
            
            if total_cost >= threshold:
                sum_apply += 1
            else:
                sum_price += total_cost
        
        if sum_apply > answer[0]:
            answer[0] = sum_apply
            answer[1] = sum_price
        elif sum_apply == answer[0]:
            answer[1] = max(answer[1], sum_price)
    
    return answer