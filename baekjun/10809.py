from string import ascii_lowercase

alpha_list = list(ascii_lowercase)
S = input()
result = ''

for alpha in alpha_list:
    if alpha in S:
        tmp = str(S.find(alpha)) + " " 
        result += tmp
    
    else:
        result += '-1 '

print(result)