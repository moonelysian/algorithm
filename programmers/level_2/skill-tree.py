# 문제 설명
# 선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.

# 예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 
# 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.
# 위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 

# 선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 
# 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.

def solution(skill, skill_trees):
    answer = 0
    for str in skill_trees:
        temp = ""       
        check = True     

        for s in str:
            if skill.find(s) != -1:
                temp += s

        for i in range(len(temp)):
            if skill[i] != temp[i]:
                check = False
                break

        if check == True:
            answer += 1

    return answer

# 다른 풀이
# def solution(skill, skill_trees):
#     answer = 0

#     for skills in skill_trees:
#         skill_list = list(skill)

#         for s in skills:
#             if s in skill:
#                 if s != skill_list.pop(0):
#                     break
#         else:
#             answer += 1

#     return answer
