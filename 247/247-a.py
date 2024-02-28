import sys
input = sys.stdin.readline
 
def main():
    x = int(input())
 
    x = int(x/10)
    print(f"{x:04}")
    
 
if __name__ == "__main__":
    main()