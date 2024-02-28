import sys
input = sys.stdin.readline

def my_find(l, x):
    if x in l:
        return l.index(x)
    else:
        return -1

def main():
    S = input().rstrip()
    abc_list = ["A", "B", "C"]
    index=0
    
    for s in S:
        index = my_find(abc_list, s)
        
        if index == -1:
            print("No")
            return
        
        abc_list = abc_list[index:]
    
    print("Yes")
    
if __name__ == "__main__":
    main()