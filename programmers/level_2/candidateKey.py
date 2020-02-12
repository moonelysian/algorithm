import pandas as pd
from itertools import combinations
def solution(relation):
    answer = []
    # 주어진 리스트를 데이터프레임으로 변환
    df = pd.DataFrame(relation)
    
    # column 리스트, column 개수
    col_list, total_col = set(df.columns), len(df.columns)
    
    # df의 row 개수. 이 개수가 유지되어야 key로 기능할 수 있다.
    unique = len(df)
    
    for i in range(1, len(col_list) + 1):
        # 가능한 key 조합을 1부터 column 개수까지 하나씩 생성
        candidate = list(combinations(col_list, i))
        
        # 각 조합마다 검증
        for value in candidate:
            # 해당 key 조합으로 table을 만들었을 때 row의 개수
            temp = len(df[list(value)].apply(lambda x: "".join(x), axis = 1).unique())
            # 만약 key가 조건을 만족하는 경우 = row 개수가 unique와 동일하다.
            if temp == unique:
                is_exist = False
                # 기존 키 값에 혹시 중복된 게 있는지.
                # 중복된 게 있다면 사용할 수 없다. 이 경우 최소성을 만족하지 않음.
                for check in answer:
                    if check & set(list(value)) == check:
                        is_exist = True
                        break
                # 최소성을 만족한다면 answer에 해당 key 조합을 추가한다.
                if is_exist == False:
                    answer.append(set(list(value)))
                    
    return len(answer)

solution([["100","ryan","music","2"],
["200","apeach","math","2"],
["300","tube","computer","3"],
["400","con","computer","4"],
["500","muzi","music","3"],
["600","apeach","music","2"]])