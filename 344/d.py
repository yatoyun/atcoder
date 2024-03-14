import sys
input = sys.stdin.readline

def main():
    T = input().strip()
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(set((input().strip().split())[1:])))
    
    T_dict = {}
    for i in range(len(T)+1):
        T_dict[T[:i]] = 10**9
    
    
    T_dict[""] = 0
    for i in range(len(A)):
        for k in range(len(T)-1,-1,-1):
            for s in A[i]:
                concat = T[:k] + s
                if concat not in T_dict:
                    continue
                T_dict[concat] = min(T_dict[T[:k]]+1, T_dict[concat])
    
    print(T_dict[T] if T_dict[T] != 10**9 else -1)
    
    

if __name__ == "__main__":
    main()