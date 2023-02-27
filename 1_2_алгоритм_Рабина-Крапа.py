import math as m
import time
start = time.time()
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


def podrostki(n,k):
    count = 0
    for i in range(0,len(k)-1):
        if hush(k[i]+k[i+1]) == hush(n):
            count+=1
    return count


#хэш функция
def hush(n):
    a = 10
    m = 1
    hush = int(n[0]) *( a**(m)) + int(n[1]) * (a**(m-1))
    return hush

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
end = time.time()
print(end - start)




