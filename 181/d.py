import sys
from collections import Counter
input = sys.stdin.readline

def is_possible(count, num):
    count_num = Counter(str(num))
    return not count_num - count

def main():
    S = input().strip()
    
    count = Counter(S)
    
    if len(S) <= 2:
        if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
            print("Yes")
        else:
            print("No")
        exit()
    
    start = 14
    while True:
        if start * 8 > 999:
            break
        if is_possible(count, start*8):
            print("Yes")
            exit()
        start += 1
    print("No")
    

if __name__ == "__main__":
    main()
