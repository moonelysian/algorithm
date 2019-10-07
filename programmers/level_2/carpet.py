import math

def solution(brown, red):
    total = brown + red
    carpet = []

    sq = int(math.sqrt(total))

    for i in range(3,sq+1):
        height = i
        width = total//i

        if (height*width) == total:
            red_w = width-2
            red_h = height-2

            if (red_h*red_w) == red:
                carpet.append(width)
                carpet.append(height)
                break

    return carpet