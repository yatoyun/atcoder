from collections import deque

def solve(S, N):
    N_2 = format(N, "b")
    N_2_len = len(N_2)

    ans = ""
    if N_2_len > len(S):
        ans = S.replace("?", "1")
        return int(ans, 2)

    for i in range(len(S) - N_2_len):
        if S[i] == "1":
            print(-1)
            exit(0)

    S = S[len(S) - N_2_len :]
    question_stack = deque()
    i = 0
    while i < len(S):
        # print(ans, question_stack)
        if S[i] == "?" and N_2[i] == "1":
            question_stack.append(i)
        if len(ans) == 0 or int(ans) == int(N_2[:i]):
            if S[i] == "?":
                ans += N_2[i]
            else:
                if S[i] > N_2[i]:
                    if len(question_stack) == 0:
                        print(-1)
                        exit(0)
                    i = question_stack.pop()
                    ans = ans[:i]+"0"
                    i += 1
                    continue
                ans += S[i]

        elif int(ans) < int(N_2[:i]):
            if S[i] == "?":
                ans += "1"
            else:
                ans += S[i]
        i += 1

    return int(ans, 2)


if __name__ == "__main__":
    S = input()
    N = int(input())
    print(solve(S, N))
