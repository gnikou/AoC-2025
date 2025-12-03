file = 'input.txt'
inp = []

with open(file) as f:
    inp = f.read().splitlines()
    
dial = 50
pass1 = 0
pass2 = 0
for i in inp:

    if i[0] == 'R':
        dial += int(i[1:])
        if dial%100:
            pass2 += int(dial/100)
        elif not dial%100 and dial > 100:
            pass2 += int(dial/100)-1
        
    else:
        prev = True if dial else False
        dial -= int(i[1:])
        if dial < 0 and prev:
            comb = 100 - dial
            if comb%100:
                pass2 += int(comb/100)
            elif not comb%100 and comb > 100:
                pass2 += int(comb/100)-1
        elif dial < 0 and not prev:
            comb = 100 - dial
            if comb%100:
                pass2 += int(comb/100)-1
            elif not comb%100 and comb > 100:
                pass2 += int(comb/100)-2

    dial = dial%100
    if not dial:
        pass1+=1
        pass2+=1

print(pass1)
print(pass2)