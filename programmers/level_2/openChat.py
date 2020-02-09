def solution(record):
    user = {}
    inout = []
    answer = []
    for r in record:
        if(r.split()[0] == "Enter"):
            user[ r.split()[1] ] = r.split()[2]
            inout.append(('in', r.split()[1]))
        elif(r.split()[0] == "Leave"):
            inout.append(('out', r.split()[1]))
        else:
            user[r.split()[1]] = r.split()[2]

    for io in inout:
        if io[0] == 'in':
            answer.append(user[io[1]] + "님이 들어왔습니다.")
        else:
            answer.append(user[io[1]] + "님이 나갔습니다.")

    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])