def solution(s):
    shortest = s
    shortenWord = s

    for index in range(1, len(s+1)//2):
        shortenWord = getShortenWord(s, index)
        if (len(shortenWord) < len(shortest)):
            shortest = shortenWord
    return len(shortest)


def getShortenWord(original, partSize):
    particalArr = []
    for i in range(len(original)//partSize):
         particalArr.append(
        	original[i*partSize:min((i+1)*partSize, len(original))]
        )
     
    buffer = ''
    count = 1

    for subStr in particalArr:
        if(buffer == subStr):
            count += 1 

        else:
            if(not(buffer=='')):
                if(count == 1):
                    count = ''
                shortenWord += str(count) + buffer
            count = 1
            buffer = subStr   

    if(count==1):
        shortenWord += buffer

    else:
        shortenWord += str(count) + buffer  
        
    return shortenWord