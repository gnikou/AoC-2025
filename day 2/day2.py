file = 'input.txt'
inp = []
with open(file) as f:
    inp = f.read()

inp = inp.split(',')
invalid = 0
invalid2 = 0
                
for i in inp:
    for num in range(int(i.split('-')[0]), int(i.split('-')[1])+1):
        num = str(num)
        if not len(num)%2:
            if num[:int((len(num)/2))] == num[int((len(num)/2)):]:
                invalid += int(num)
                invalid2 += int(num)
                continue
        
        for j in range(int(len(num)/2)):
            j = j+1
            number = num
            for _ in range(len(num)):
                if number==num[:j]:
                    invalid2 += int(num)
                    break
                elif number[:j] == number[j:2*j]:
                    number = str(int(number) - (int(number[:j])*10**(len(number)-j)))
print(invalid)
print(invalid2)

