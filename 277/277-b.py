import sys
input = sys.stdin.readline

first_not_word_list = ["H" , "D" , "C" , "S"]
second_not_word_list = ["A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K"]

def check_word(word, word_list):
    if word[0] not in first_not_word_list:
        return False
    elif word[1] not in second_not_word_list:
        return False
    elif word in word_list:
        return False

    return True



def main():
    N = int(input())

    word_list = []
    for _ in range(N):
        S = input()
        if check_word(S, word_list):
            word_list.append(S)
        else:
            print("No")
            return 0

    print("Yes")

if __name__ == "__main__":
    main()