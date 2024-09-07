from math import ceil

def calculate_fee(time, fees):
    default_time, default_fee, unit_time, unit_fee = fees
    if time <= default_time:
        return default_fee
    return default_fee + ceil((time - default_time) / unit_time) * unit_fee

def solution(fees, records):
    parking = {}  # 입차된 차량의 번호와 입차 시간을 저장
    total_time = {}  # 각 차량의 총 주차 시간을 저장

    for record in records:
        time_str, car_number, action = record.split()
        hour, minute = map(int, time_str.split(":"))
        time = hour * 60 + minute

        if action == "IN":
            parking[car_number] = time
        elif action == "OUT":
            parked_time = time - parking.pop(car_number)
            total_time[car_number] = total_time.get(car_number, 0) + parked_time 
            # get() 메서드는 딕셔너리에서 키(car_number)에 해당하는 값을 반환.
            # 만약 그 키가 딕셔너리에 없으면, 두 번째 인자로 제공된 기본값(0)을 반환
            # 즉, total_time.get(car_number, 0)은 total_time 딕셔너리에서 해당 차량 번호의 주차 시간을 가져오거나, 그 차량 번호가 딕셔너리에 아직 없다면 0을 반환.

    # 출차 기록이 없는 차량 처리 (23:59에 출차된 것으로 계산)
    for car_number, time in parking.items():
        parked_time = 1439 - time  # 23:59 = 1439 minutes
        total_time[car_number] = total_time.get(car_number, 0) + parked_time

    # 각 차량의 요금을 계산하여 결과 리스트에 추가
    answer = []
    for car_number in sorted(total_time):
        fee = calculate_fee(total_time[car_number], fees)
        answer.append(fee)

    return answer

