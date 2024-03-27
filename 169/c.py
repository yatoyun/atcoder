import sys
input = sys.stdin.readline

def main():
    A, B = input().split()
    A = int(A)
    
    num = len(B)
    B = int(B.replace(".", ""))
    print(A * B // 10**(num-2))    
    
        
    

if __name__ == "__main__":
    main()
