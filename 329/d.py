import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    
    A = list(map(int, input().split()))
    
    max_votes = 0
    max_vote_candidate = 1
    vote_dict = defaultdict(int)
    
    for i in range(M):
        vote = A[i]
        vote_dict[vote] += 1
        if vote_dict[vote] > max_votes:
            max_votes = vote_dict[vote]
            max_vote_candidate = vote
        elif vote_dict[vote] == max_votes and vote < max_vote_candidate:
            max_vote_candidate = vote
        print(max_vote_candidate)
        
    
    
    
    

if __name__ == "__main__":
    main()