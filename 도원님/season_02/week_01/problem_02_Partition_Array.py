https://www.acmicpc.net/problem/1208와 유사한 문제
meet in the middle 개념 자체가 익숙치 않아서 떠올리지조차 못한 문제
개념을 익히고 나서도 이분탐색으로 추가 최적화 작업이 필요했다.

import bisect
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        N = len(nums)//2
        S = sum(nums)
        L1 = nums[:N]
        L2 = nums[N:]
        dic1 = [set() for i in range(N+1)]
        dic2 = [set() for i in range(N+1)]
        
        dic1[0].add(0)
        dic2[0].add(0)
        for i in range(N): # i번째 숫자를 더할 것
            for j in range(i,-1,-1):
                
                for k in dic1[j]:
                    dic1[j+1].add(k+L1[i])

                for k in dic2[j]:
                    dic2[j+1].add(k+L2[i])

        answer = 3000000000000
        for i in range(N+1):
            dic1[i] = sorted(dic1[i])
            dic2[i] = sorted(dic2[i])
        for i in range(N+1):
            sl1 = dic1[i]
            sl2 = dic2[N-i]
            for j in sl1:
                match_idx = bisect.bisect_left(sl2,S//2-j)
                cnt = j+sl2[min(match_idx,len(sl2)-1)]
                if cnt>=(S+1)//2:
                    answer = min(answer,cnt)


        return 2*answer-S
		
