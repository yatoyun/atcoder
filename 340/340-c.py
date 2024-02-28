import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    n = int(input())
    
    nums = set([n])
    nums_dict = defaultdict(int)
    nums_dict[n] = 1
    
    while len(nums) > 0:
        next_nums = set()
        for num in nums:
            if num == 1:
                continue
            
            if num % 2 == 0:
                next_nums.add(num // 2)
                nums_dict[num // 2] += nums_dict[num] * 2
            else:
                next_nums.add(num // 2)
                next_nums.add(num // 2 + 1)
                nums_dict[num // 2] += nums_dict[num]
                nums_dict[num // 2 + 1] += nums_dict[num]
        nums = next_nums
    
    ans = 0
    for key, value in nums_dict.items():
        if key == 1:
            continue
        ans += key * value
    print(ans)

if __name__ == "__main__":
    main()