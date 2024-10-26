def solution(bandage, health, attacks):
    answer = 0
    t, x, y = bandage[0], bandage[1], bandage[2]
    
    time = 0
    attack_idx = 0
    my_health = health
    attack_success = 0
    while time <= attacks[-1][0]:
        if time == attacks[attack_idx][0]:
            my_health -= attacks[attack_idx][1]
            attack_idx += 1
            attack_success = 0
            if my_health <= 0:
                break
        else:
            if my_health < health and attack_success <= t:
                my_health = min(health, my_health + x)
                attack_success += 1
                if attack_success == t:
                    my_health = min(health, my_health + y)
                    attack_success = 0

        #print(time, my_health, (time - last_attack_time))
        time += 1
    if my_health <= 0:
        return -1
    return my_health