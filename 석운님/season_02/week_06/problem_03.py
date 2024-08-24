import math

def solution(fees, records):
    answer = []
    history = {}
    car_list = []
    for r in records:
        s = r.split()
        min = s[0].split(':')
        min = int(min[0])*60 + int(min[1])
        if s[1] in history:
            history[s[1]].append(min)
        else:
            history[s[1]] = [min]
            car_list.append(s[1])
    car_list = sorted(car_list)
    for car in car_list:
        total_fee = 0
        total_time = 0
        li = history[car]
        while len(li) > 1:
            tin = li.pop(0)
            tout = li.pop(0)
            total_time += (tout - tin)
            
        if li:
            last = 23 * 60 + 59
            total_time += last - li[0]
        if total_time <= fees[0]:
            total_fee += fees[1]
        else:
            total_fee += (fees[1] + math.ceil((total_time - fees[0])/fees[2])*fees[3])
        answer.append(total_fee)
            
    return answer