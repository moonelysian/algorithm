import queue

N = int(input())
q = queue.Queue()

for i in range(N):
    q.put(i+1)

while(q.qsize()!=1):
    q.get()
    tmp=q.get()
    q.put(tmp)

print(q.get())

    