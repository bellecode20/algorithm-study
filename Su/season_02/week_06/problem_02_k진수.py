# [후보 선정]
# 0P0처럼 소수 양쪽에 0이 있는 경우
# P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
# 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
# P처럼 소수 양쪽에 아무것도 없는 경우
# 단, P는 각 자릿수에 0을 포함하지 않는 소수입니다.
# 예를 들어, 101은 P가 될 수 없습니다.

# 1. split
# 2. K진수로 바꾸고
# 3. 소수 판별


# [k진수 변환]
# 10진수를 k진수로 변환하는 방법
def k_num(n,k):
    if k == 10:
        return n
    else:
        new_n = ""
        while n > 0:
            new_n += str(n % k) # 10진법 수를 n으로 나눈 나머지를 변수에 저장하고
            n = n // k
        return new_n[::-1] # 거꾸로 읽기

# [소수 판별]
# 2부터 n의 루트까지 수를 나눠본다.
# 나누어 떨어지는 경우가 있는 경우 False
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    num = k_num(n,k)
    nums = str(num).split("0")
    for x in nums:
        #x가 비어있는 경우 예외처리
        if x and isPrime(int(x)):
            answer += 1
    return answer
