import sys
input = sys.stdin.readline

def mis_under_time(h,m):
    if h//10==1 or h//10==0:
        if h%10 <= 5:
            return True

    else:
        if m//10 <= 3:
            return True

    return False

h, m = map(int, input().split())

if mis_under_time(h,m):
    print(h,m)

else:
    minutes = h*60 + m
    while True:
        minutes += 1
        if minutes >= 23*60+59:
            minutes = 0
        if mis_under_time(minutes//60, minutes%60):
            print(minutes//60, minutes%60)
            break