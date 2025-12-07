file = 'input.txt'

inp = []

with open(file) as f:
    inp = f.read().splitlines()
    
score1 = 0
score2 = 0
for i in inp:
    number=[]
    first_num = 0 
    second_num = 0

    for j in range(len(i)):
        num = [int(x) for x in list(i)]
        if num[j] > first_num and j<len(i)-1:
            first_num = num[j]
            second_num = 0
        elif num[j] == first_num:
            second_num = num[j]
        elif num[j] > second_num:
            second_num = num[j]
    score1 += (first_num*10) + second_num
    
    num = [int(x) for x in list(i)]
    id = 0
    id2 = 0
    for k in range(12):
        largest = 0
        id2 += id
        for idx, l  in enumerate(num[id2: len(num)-11+k]):
            if l > largest:
                id = idx+1
                largest = l
        number.append(largest)

    jolt = int(''.join(f'{i}' for i in number))
    score2 += jolt

            
print(score1)
print(score2)