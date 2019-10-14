from collections import Counter # 배열요소를 카운트해서 딕셔너리로 변환

def solution(clothes):
    clothesDict = Counter( key for value, key in clothes)
    result = 1

    for key in clothesDict:
        result *= (clothesDict[key]+1)
    
    #어떤 옷도 착용하지않는 경우 제외
    return result-1
