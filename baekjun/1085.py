rec = input()
rec = rec.split()
rec = [ int(rec[i]) for i in range(4) ]

x = rec[0]
y = rec[1]
w_x=rec[2]-rec[0]
h_y=rec[3]-rec[1]

length = [x,y,w_x,h_y]

print(min(length))
