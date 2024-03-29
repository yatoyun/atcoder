import sys
from itertools import permutations
input = sys.stdin.readline

def main():
    grid = [list(map(int,input().split())) for _ in range(3)]
    
    pass_count = 0
    for perm in permutations(range(9)):
        check_row = [(0,-1)]*3
        check_col = [(0,-1)]*3
        check_diag = [(0,-1)]*2
        flag = True
        
        for i in perm:
            y, x = i//3, i%3
            crr = grid[y][x]
            # row
            if check_row[y][0] == 1 and check_row[y][1] == crr:
                flag = False
                break
            check_row[y] = (check_row[y][0]+1, crr)
                
            # col
            if check_col[x][0]==1 and check_col[x][1] == crr:
                flag = False
                break
            check_col[x] = (check_col[x][0]+1, crr)
            
            # diag
            if y == x:
                if check_diag[0][0]==1 and check_diag[0][1] == crr:
                    flag = False
                    break
                check_diag[0] = (check_diag[0][0]+1, crr)
            if y + x == 2:
                if check_diag[1][0]==1 and check_diag[1][1] == crr:
                    flag = False
                    break
                check_diag[1] = (check_diag[1][0]+1, crr)
        if flag:
            pass_count += 1
    
    print(pass_count/362880)
            
            

if __name__ == "__main__":
    main()