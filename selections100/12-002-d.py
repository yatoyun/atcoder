import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    
    relation_set = set()
    for _ in range(M):
        relation_set.add(tuple(input().rstrip()))
    ans = 0
    for bit in range(1<<N):
        members = []
        for i in range(N):
            if bit & (1<<i):
                members.append(i+1)
            
            flag = True
            for i in range(len(members)):
                for j in range(i+1, len(members)):
                    if tuple(str(members[i]) + " " + str(members[j])) not in relation_set:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                ans = max(ans, len(members))
    print(ans)

if __name__ == "__main__":
    main()