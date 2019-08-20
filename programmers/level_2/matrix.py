import numpy as np

def solution(arr1, arr2):
    answer = (np.matrix(arr1)*np.matrix(arr2)).tolist()
    print(answer)
    return answer

solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]])

#다른 풀이
# def productMatrix(A, B):
#     return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]