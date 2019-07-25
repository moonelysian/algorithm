from sys import stdin

N = int(stdin.readline())
arr = []
for i in range(N):
    arr.append(int(stdin.readline()))

arr.sort()
for a in arr:
    print(a)

# 병합정렬을 직접 구현 but 시간초과
# def merge_sort(list):
#     if len(list) <= 1:
#         return list
    
#     mid = len(list)//2
    
#     leftList = list[:mid]
#     rightList = list[mid:]
    
#     leftList = merge_sort(leftList)
#     rightList = merge_sort(rightList)

#     return merge(leftList,rightList)

# def merge(left, right):
#     sortedList = []
#     while len(left) > 0 or len(right) > 0:
#         if len(left) > 0 and len(right) > 0:
#             if left[0] <= right[0]:
#                 sortedList.append(left[0])
#                 left = left[1:]
#             else:
#                 sortedList.append(right[0])
#                 right = right[1:]
#         elif len(left) > 0:
#             sortedList.append(left[0])
#             left = left[1:]
#         elif len(right) > 0:
#             sortedList.append(right[0])
#             right = right[1:]
#     return sortedList

# result = merge_sort(unsorted)

# for i in result:
#     print(i)
