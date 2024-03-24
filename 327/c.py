import sys
input = sys.stdin.readline

def main():
    A = []
    for _ in range(9):
        row = list(map(int, input().split()))
        if len(set(row)) != 9:
            print("No")
            return
        A.append(row)
    
    for i in range(9):
        col = [A[j][i] for j in range(9)]
        if len(set(col)) != 9:
            print("No")
            return
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [A[i + k][j + l] for k in range(3) for l in range(3)]
            if len(set(block)) != 9:
                print("No")
                return
    print("Yes")
    
    

if __name__ == "__main__":
    main()