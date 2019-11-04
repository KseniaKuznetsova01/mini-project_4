# Игра, в которой игрок угадывает слова по вопросам, либо один игрок загадывает слово, а другой должен его отгадать.
import local as lc
print(lc.HI)
print(lc.N)
d = int(input())
m = 0
if d == 1:
    print(lc.F)
    f = int(input())
    if f == 1:
        print(lc.F1)
        s = lc.F1_1
    elif f == 2:
        print(lc.F2)
        s = lc.F2_2
    elif f == 3:
        print(lc.F3)
        s = lc.F3_3
    elif f == 4:
        print(lc.F4)
        s = lc.F4_4
    elif f == 5:
        print(lc.F5)
        s = lc.F5_5
    elif f == 6:
        print(lc.F6)
        s = lc.F6_6
    elif f == 7:
        print(lc.F7)
        s = lc.F7_7
    elif f == 8:
        print(lc.F8)
        s = lc.F8_8
    elif f == 9:
        print(lc.F9)
        s = lc.F9_9
    else:
        print(lc.F10)
        s = lc.F10_10
else:
    print(lc.S)
    s = input()
f = s
s = s.lower()
a = len(s)

s1 = '_ ' * a
print(s1)
r = ' '
osh = 1
print(lc.OSH)
print(lc.OTG)
while osh <= 5 and m != a:
    print(lc.B)
    b = input()
    bc = s.find(b)
    if bc != -1:
        print(lc.U)
        c = bc * 2
        v1 = a * 2 - c - 1
        v = a * 2 - v1 - 1
        s1 = s1[0:v] + s[bc] + s1[v + 1:]
        print(s1)
        r1 = int(v / 2)
        r2 = int((v / 2) + 1)
        s = s[0:r1] + r + s[r2:]
        m += 1
    else:
        print(lc.NU)
        osh += 1
        print(6-osh)

if osh != 5 and osh < 5:
    print(lc.KON)
else:
    print(lc.FAIL)
    print(f)