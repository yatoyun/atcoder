import sys
input = sys.stdin.readline

def check_dis(a, b, nodes):
    dis = abs(nodes[a] - nodes[b])
    if dis > 2:
        dis = 5-dis
    return dis

def main():
    nodes = {"A":0, "B":1, "C":2, "D":3, "E":4}
    
    s = input()
    t = input()
    
    s_dis = check_dis(s[0], s[1], nodes)
    t_dis = check_dis(t[0], t[1], nodes)
    if s_dis == t_dis:
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()