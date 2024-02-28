import sys
input = sys.stdin.readline

def calc(a, b):
    return (a**3 + a**2 * b + a * b**2 + b**3)

def main():
    n = int(input())

    print("a|\t\t      b|\tresult")

    for i in range(10):
        num = []
        for j in range(10):
            if calc(i,j) > n:
                num.append(j)
        num.sort()
        list = [str(a) for a in num]
        list = " ".join(list)
        print(f"{i}| {list: >20}|\t{calc(i,num[0])}")

if __name__ == "__main__":
    main()