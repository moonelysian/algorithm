def solution(s):
    textList = s.split(' ')
    arr = []

    for text in textList:
        text = text.capitalize()
        arr.append(text)

    answer = ' '.join(arr)

    return answer
