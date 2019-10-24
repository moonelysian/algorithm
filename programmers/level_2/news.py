from collections import Counter

def preprocess(content):
    arr = []
    for i in range(len(content)-1):
        if content[i:i+2].isalpha():
            arr.append(content[i:i+2])
    return arr

def solution(str1, str2):
    
    str1 = str1.lower()
    str2 = str2.lower()

    if str1 == str2:
        return 65536

    str1 = preprocess(str1)
    str2 = preprocess(str2)

    counter1 = Counter(str1)
    counter2 = Counter(str2)

    intersection = counter1 & counter2
    union = counter1 | counter2
    
    intersection = sum(list(intersection.values()))
    union = sum(list(union.values()))

    answer = int(intersection/union*65536)

    return answer

solution("aa1+aa2", "AAAA12")