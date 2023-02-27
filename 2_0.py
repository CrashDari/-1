f_d= open('smile_demo.txt', 'r',encoding="utf8")
d = f_d.read().split()
f_o= open('smile_original.txt', 'r',encoding="utf8")
o = f_o.read().split()

def ln(sp):
    count = 0
    for a in sp:
        count +=len(a)
    return count

def pl(n,k):
    count = 0
    for i in range(0,len(k)-2):
        if k[i+2] == n[len(k[i])+len(k[i+1]): len(k[i])+len(k[i+1])+ len(k[i+2])] :
            if k[i+1] ==  n[len(k[i]):len(k[i])+len(k[i+1])]:
                if k[i] == n[0:len(k[i])]:
                    count+=len(n)
    return count

def sump(d):
    plagiat = 0
    for i in range(0,len(d)-2):
        plagiat+= pl(d[i]+d[i+1]+d[i+2],o)
    return plagiat

plagiat = sump(d)
original =  ln(o)
print('Количество символов в оригинальном тексте:   ',original)
print('Количество списанных символов в реферате:   ',plagiat)
print('Кол-во плагиата:   ',round(plagiat/original *100,2), '%')
f_d.close()
f_o.close()

