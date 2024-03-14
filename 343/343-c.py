import sys
input = sys.stdin.readline

def main():
    n = int(input())

    ans = 0
    num = 1
    num_3 = 1
    while num_3 <= n:
        if num_3 % 10 == 0:
            num += 1
            num_3 = num ** 3
            continue
        num_str = str(num_3)
        flag = True
        for i in range(len(num_str)//2):
            
            if num_str[i] != num_str[-i-1]:
                flag = False
                break
        if flag:
            ans = num_3
            
        
        num += 1
        num_3 = num ** 3
    
    print(ans)

if __name__ == "__main__":
    main()
