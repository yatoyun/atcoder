import sys
input = sys.stdin.readline

# ans 1
# def main():
#     n = int(input())
    
#     for i in range(n+1):
#         for j in range(n+1):
#             for k in range(n+1):
#                 if i+j+k <= n:
#                     print(i, j, k)

def main():
    n = int(input())
    
    ans = [0] * 3
    while ans[0] <= n:
        while ans[0] + ans[1] <=n:
            while sum(ans) <= n:
                print(*ans)
                ans[2] += 1
            ans[2] = 0
            ans[1] += 1
        ans[1] = 0
        ans[0] += 1

if __name__ == "__main__":
    main()