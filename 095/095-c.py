from cmath import inf
from json.encoder import INFINITY
import sys
input = sys.stdin.readline

def main():
    A, B, C, X, Y = map(int, input().split())

    ans = INFINITY

    if X > Y:
        n = X
    else:
        n = Y
    
    for ab in range(0,n*2+1):
        sm = ab * C

        x = X - int(ab/2)
        y = Y - int(ab/2)

        if x > 0:
            sm += A * x
        if y > 0:
            sm += B * y
        
        ans = min(ans, sm)
    print(ans)

if __name__ == "__main__":
    main()