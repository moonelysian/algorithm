## is VS ==
```python
x = 256
x is 256 #True

y = 257
y is 257 #False
```

`is` 는 **reference** 비교
`==` 는 **값** 비교

python에서 변수는 내부적으로 데이터를 가르키는게 아니라 인스턴스 포인터를 가르킴


*integer caching*
파이썬의 경우 [-5,256]범위의 정수(small integers)에 대해 정수 객체의 배열을 유지
이 범위 내에 해당하는 변수를 선언하면 기존 객체에 대한 reference만 반환
따라서 small integers는 같은 객체에 선언됨

```python
c = 1
d = 1
id(c) # 12345
id(d) # 12345
```

## *args & **kwargs

#### *args
여러 개의 인자를 함수로 받고자 할 때
```python
# mylist 원소의 행과 열 뒤집기
mylist=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

result = list(map(list,zip(*mylist)))
```

#### **kwargs
keyword argument의 줄임말로 키워드를 제공

```python
def intro(**kwargs):
    for key, value in kwargs.items():
        print("{0} is {1}".formant(key,value))

intro(MyName = 'Moon') 
# MyName is Moon
```
`**kwargs`는 (키워드 = 특정 값) 형태로 함수를 호출할 수 있음
그대로 딕셔너리 형태로 함수 내부로 전달
