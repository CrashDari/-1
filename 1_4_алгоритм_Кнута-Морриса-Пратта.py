import math as m
#создаём список простых чисел
def prost():
    nnn = []
    number  = 2
    while True:
        prs = True
        for x in range(2, int(m.sqrt(number)+1)):
            if number % x == 0:
                prs = False
                break
        if prs:
                nnn.append(str(number))
        number+=1
        if len(nnn) == 500:
            return nnn
        
def chisla():
    chisla  = []
    for i in range(10,100):
        chisla.append(str(i))
    return chisla


def prefix(s):
    v = [0]*len(s)
    for i in range(1,len(s)):
        k = v[i-1]
        while k > 0 and s[k] != s[i]:
            k = v[k-1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v

def kmp(s,t):
    index = -1
    f = prefix(s)
    k = 0
    for i in range(len(t)):
        while k > 0 and s[k] != t[i]:
            k = f[k-1]
        if s[k] == t[i]:
            k = k + 1
        if k == len(s):
            index = i - len(s) + 1
            break
    return index


def podrostki(n,k):
    count = 0
    for i in range(0,len(k)-1):
        if kmp(k[i]+k[i+1],n) == 0:
                count+=1
    return count



def ans(numbers):
    vlog = []
    for a in numbers:
        vlog.append([podrostki(a,ss),a])
    return vlog



def srt(k):
    m = k[0][0]
    for a in k:
        if a[0] == m:
            print(a[1], '  количество повторений:  ',  a[0])


d = prost()
ss = ''
for a in d:
    ss+=a


numbers = chisla()
vlog = ans(numbers)

vlog.sort(reverse = True)

print('Наиболее часто встречающиеся двузначные числа:  ')
srt(vlog)
















