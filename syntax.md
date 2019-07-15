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