from heapq import heapify  # , heappop, heappush, heappushpop
input()  # N = int(input())
H = [-x for x in map(int, input().split())]

heapify(H)
print("", *[-x for x in H])
