#code
import sys
input = sys.stdin.readline

def main():
    N, A, B = map(int, input().split())
    
    D = list(map(int, input().split()))
    
    day_set = set()
    for d in D:
        day_set.add(d%(A+B))
    day_list = list(day_set)
    
    day_list.sort()
    min_day = day_list[0]
    max_day = day_list[-1]
    if max_day - min_day + 1 <= A:
        print("Yes")
        return

    for i in range(len(day_list)-1):
        left = day_list[i]+1
        right = A+B - day_list[i+1] + 1
        if left + right <= A:
            print("Yes")
            return
    print("No")
            

if __name__ == "__main__":
    main()