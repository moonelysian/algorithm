def solution(cacheSize, cities):
    cache = []
    answer = 0
    cities = [ city.upper() for city in cities ]
    if (cacheSize != 0):
        for city in cities:
            if (city in cache):
                answer += 1
                cache.pop(cache.index(city))
                cache.append(city)
            else:
                if(len(cache) < cacheSize):
                    cache.append(city)
                else:
                    cache.pop(0)
                    cache.append(city)
                answer += 5
    else:
        answer = len(cities)*5
    return answer

solution(3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul'])