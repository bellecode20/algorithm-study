def solution(n, arr1, arr2):
    answer = []
    def get_converted(arr):
        new_list = []
        for num in arr:
            new_str = bin(num).replace("0b", "").zfill(n)
            new_list.append(list(new_str))
        return new_list
    
    new_arr1, new_arr2 = get_converted(arr1), get_converted(arr2)

    for i in range(n):
        temp = ""
        for j in range(n):
            if new_arr1[i][j] == "0" and new_arr2[i][j] == "0":
                temp += " "
            else:
                temp += "#"
        answer.append(temp)
        
    return answer