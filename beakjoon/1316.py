N = int(input())
count = N
for _ in range(N):
    word = input()
    check = []
    
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            count-=1
            break
print(count)