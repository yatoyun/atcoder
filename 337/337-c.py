import sys
input = sys.stdin.readline

def main():
    head_dict = dict()
    n = int(input())
    
    A = list(map(int, input().rstrip().split()))
    
    for i, a in enumerate(A):
        head_dict[a] = i+1
    
    head = head_dict[-1]
    print(head, end=" ")
    for i in range(n-1):
        head = head_dict[head]
        print(head, end=" ")
        
if __name__ == "__main__":
    main()