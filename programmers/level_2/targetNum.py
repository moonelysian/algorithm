def solution(numbers, target):
    answer = 0
    len_numbers = len(numbers)

    def operator(index=0):
        if index < len_numbers:
            numbers[index] *= 1
            operator(index+1)

            numbers[index]*=(-1)
            operator(index+1)
        
        elif sum(numbers) == target:
            nonlocal answer
            answer += 1
    
    operator()
    print(answer)
    return answer

numbers = [1,1,1,1,1]
target = 3

solution(numbers,target)