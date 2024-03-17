import sys
input = sys.stdin.readline

def main():
    D = int(input())
    ans = 10**13
    
    num_list = []
    for a in range(0, int(pow(D, 1/2))+1):
        num_list.append(a)
    
    l = 0
    r = len(num_list)-1
    while l <= r:
        sum_num = num_list[l]**2 + num_list[r]**2
        if abs(sum_num-D) < ans:
            ans = abs(sum_num-D)
        
        if sum_num < D:
            l += 1
        else:
            r -= 1
            
    print(ans)

if __name__ == "__main__":
    main()