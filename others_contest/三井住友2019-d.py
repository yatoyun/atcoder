import sys
import itertools
input = sys.stdin.readline

def main():
    N = int(input())
    S = input()
    
    ans = 0

    #100の位
    for i in range(10):
        now_i = S.find(str(i))
        if now_i == -1 or now_i >= N-2:
            continue

        for j in range(10):
            now_j = S.find(str(j), now_i+1)
            if now_j == -1 or now_j >= N-1:
                continue

            for k in range(10):
                now_k = S.find(str(k),now_j+1)
                if now_k != -1:
                    ans += 1
    print(ans)

if __name__ == "__main__":
    main()