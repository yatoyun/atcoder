import sys
input = sys.stdin.readline

def main():
    S = input().strip()
    
    stack = []
    for s in S:
        stack.append(s)
        if len(stack) >= 3 and stack[-3:] == ["A", "B", "C"]:
            stack.pop()
            stack.pop()
            stack.pop()
    print("".join(stack))

if __name__ == "__main__":
    main()