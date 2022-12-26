def base10to(n, b): # 10進数nをb進数に変換
    if (int(n/b)):
        return base10to(int(n/b), b) + str(n%b)
    return str(n%b)

def base10from(num, b): # b進数numを10進数に変換
    n = 0
    numlist = list(num);
    while (numlist):
        n *= b
        n += int(numlist.pop(0))
    return n

def factor2(num): # numが何回2で割れるかを調べる
    n = 0
    num1 = int(num)
    while True:
        if num1 % 2 == 0:
            n += 1
            num1 = num1 / 2
        else:
            break
    return n

i = 1
index2 = 0
while i <= 10**20:
    numstr = str(base10to(i, 3))
    if "0" in numstr:
        pass
    else:
        # tmp_index2 = factor2(numstr)
        if numstr[-1] == "2": # and tmp_index2 > index2:
            # index2 = tmp_index2
            with open("factor2.txt", mode='a') as f2:
                print(numstr,factor2(numstr),file=f2)
    i += 1
