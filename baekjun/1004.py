import math

T = int(input()) # 테스트 개수 입력

for trials in range(T):

    # 도착 및 출발 위치를 받아서 변수에 집어넣음
    x1, y1, x2, y2 = map(int, input().split(' '))

    n = int(input()) # 행성 개수

    planets = [] # 행성 좌표 및 반지름이 들어갈 리스트

    # 좌표를 입력 받아서 리스트로 만듦
    for i in range(n):
        planets.append(input())

    # shell_1 은 출발지점이 속한 행성의 숫자
    # shell_2 은 도착지점이 속한 행성의 숫자
    # shell_3 은 출발 및 도착 지점이 함께 속한 행성의 숫자

    shell_1 = 0
    shell_2 = 0
    shell_shared = 0

    # 입력 받은 행성들에 대해 루프를 돌림
    for planet in planets:

        planet = planet.split(' ')

        xc = int(planet[0])
        yc = int(planet[1])
        r = int(planet[2])

        d1 = math.sqrt((xc - x1) ** 2 + (yc - y1) ** 2)  # 행성과 출발지점과의 거리
        d2 = math.sqrt((xc - x2) ** 2 + (yc - y2) ** 2)  # 행성과 도착지점과의 거리

        # 행성 중심과 출발/도착 지점과의 거리가 반지름보다 작으면
        # 그 행성에 속한 것으로 구분하여 해당 shell 값에 +1
        if d1<r and d2<r:
            shell_1 += 1
            shell_2 += 1
            shell_shared += 1

        else:
            if d1 < r :
                shell_1 += 1
            if d2 < r :
                shell_2 += 1

    # '출발/도착 지점이 함께 들어있는 있는 행성'에 의한 경계선의 값을 빼고 리턴하도록 함.
    print(shell_1 + shell_2 - shell_shared*2)   
