def solution(survey, choices):
    answer = ''
    score = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0,
    }
    for i, choice in enumerate(choices):
        if choice >= 1 and choice <= 3:
            score[survey[i][0]] += (3 - choice + 1)
        elif choice <= 7 and choice >= 5:
            score[survey[i][1]] += (choice - 4)
        else:
            continue
            
    if score["R"] >= score["T"]:
        answer += "R"
    else:
        answer += "T"
    if score["C"] >= score["F"]:
        answer += "C"
    else:
        answer += "F"
    if score["J"] >= score["M"]:
        answer += "J"
    else:
        answer += "M"
    if score["A"] >= score["N"]:
        answer += "A"
    else:
        answer += "N"
    return answer