num = int(input())
divisor = input()
divisor = divisor.split()
divisor = [ int(divisor[i]) for i in range(num) ]
print(max(divisor)*min(divisor))