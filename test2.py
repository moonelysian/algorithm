def playlist(songs):
    # Write your code here
    count = 0
    for i in range(len(songs)):
        print("i: ",i)
        if(songs[i]%60 == 0):
            songs[i] = 0
            count += 1
        else:
            for j in range(i+1,len(songs)):
                print("j: ",j)
                print("ccc: ")
                if ((songs[i]+songs[j])%60 == 0):
                     count += 1 
                     songs[i]=0
                     songs[j]=0
                     print("songs: ",songs)
                     break
            print("still count: ",count)
    tmp = list(set(songs))
    tmp.remove(0)
    print(len(tmp))
    count += len(tmp)
    print(count)
    return count

playlist([10,50,90,30])