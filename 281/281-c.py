import sys
input = sys.stdin.readline

N, T = map(int, input().split())

A = list(map(int, input().split()))

music_time_sum = sum(A)

time = T % music_time_sum
for i, music in enumerate(A):
    time -= music
    if time <= 0:
        print(i + 1, time + music)
        break

