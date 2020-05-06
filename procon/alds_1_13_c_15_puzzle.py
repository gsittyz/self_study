from heapq import heappop, heappush
from copy import deepcopy
from bisect import bisect_left, insort_left

next_zero_idx = ((1, 4), (0, 2, 5), (1, 3, 6), (2, 7),
                 (0, 5, 8), (1, 4, 6, 9), (2, 5, 7, 10), (3, 6, 11),
                 (4, 9, 12), (5, 8, 10, 13), (6, 9, 11, 14), (7, 10, 15),
                 (8, 13), (9, 12, 14), (10, 13, 15), (11, 14))
answer_idx = [15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
answer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
answer_dec = 0
for i in range(16):
    answer_dec += answer[i] * (16 ** i)

idx22d = ((0, 0), (0, 1), (0, 2), (0, 3),
          (1, 0), (1, 1), (1, 2), (1, 3),
          (2, 0), (2, 1), (2, 2), (2, 3),
          (3, 0), (3, 1), (3, 2), (3, 3))
manhattan = [[0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4, 5, 3, 4, 5, 6],
             [1, 0, 1, 2, 2, 1, 2, 3, 3, 2, 3, 4, 4, 3, 4, 5],
             [2, 1, 0, 1, 3, 2, 1, 2, 4, 3, 2, 3, 5, 4, 3, 4],
             [3, 2, 1, 0, 4, 3, 2, 1, 5, 4, 3, 2, 6, 5, 4, 3],
             [1, 2, 3, 4, 0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4, 5],
             [2, 1, 2, 3, 1, 0, 1, 2, 2, 1, 2, 3, 3, 2, 3, 4],
             [3, 2, 1, 2, 2, 1, 0, 1, 3, 2, 1, 2, 4, 3, 2, 3],
             [4, 3, 2, 1, 3, 2, 1, 0, 4, 3, 2, 1, 5, 4, 3, 2],
             [2, 3, 4, 5, 1, 2, 3, 4, 0, 1, 2, 3, 1, 2, 3, 4],
             [3, 2, 3, 4, 2, 1, 2, 3, 1, 0, 1, 2, 2, 1, 2, 3],
             [4, 3, 2, 3, 3, 2, 1, 2, 2, 1, 0, 1, 3, 2, 1, 2],
             [5, 4, 3, 2, 4, 3, 2, 1, 3, 2, 1, 0, 4, 3, 2, 1],
             [3, 4, 5, 6, 2, 3, 4, 5, 1, 2, 3, 4, 0, 1, 2, 3],
             [4, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3, 1, 0, 1, 2],
             [5, 4, 3, 4, 4, 3, 2, 3, 3, 2, 1, 2, 2, 1, 0, 1],
             [6, 5, 4, 3, 5, 4, 3, 2, 4, 3, 2, 1, 3, 2, 1, 0]]
manhattan = tuple(tuple(x) for x in manhattan)


class Puzzle():
    def __init__(self, state, count=0):
        self.state = state
        self.number_idx = self.get_number_idx(state)
        self.count = count
        self.cost = self.count + self.calc_manhattan()
        self.prev_zero_idx = self.number_idx[0]

    def get_number_idx(self, state):
        number_idx = [state.index(i) for i in range(16)]
        return number_idx

    def calc_manhattan(self):
        manhattan_sum = 0
        for i in range(16):
            manhattan_sum += manhattan[self.number_idx[i]][answer_idx[i]]
        return manhattan_sum

    def get_next_zero_index(self):
        i = self.number_idx[0]
        for next_zero in next_zero_idx[i]:
            if next_zero != self.prev_zero_idx:
                yield next_zero

    def move_zero_to(self, idx):
        zero_i = self.number_idx[0]
        target_i = idx
        target = self.state[target_i]
        self.state[zero_i], self.state[target_i] = target, 0
        self.number_idx[0], self.number_idx[target] = target_i, zero_i
        self.prev_zero_idx = zero_i
        self.count += 1
        self.cost = self.count + self.calc_manhattan()

    def is_answer(self):
        return self.number_idx == answer_idx

    def print_state(self):
        for i in range(4):
            print(" ".join(list(map(str, self.state[i * 4:i * 4 + 4]))))

    def __eq__(self, other):
        return self.state == other.state

    def get_dec(self):
        dec = 0
        for i in range(16):
            dec += self.state[i] * (16 ** i)
        return dec


def solve_puzzle(state):
    init = Puzzle(state)
    if init.is_answer():
        return 0
    # if state == [1, 6, 7, 2, 5, 10, 12, 3, 0, 14, 13, 8, 9, 15, 11, 4]:
    #     return 30
    states = []
    history = []

    def index(lst, val):
        idx = bisect_left(lst, val)
        if idx < len(lst) and lst[idx] == val:
            return idx
        return -1
    dec = init.get_dec()
    heappush(states, (init.cost, init.count, dec, init))
    insort_left(history, dec)

    while True:
        puzzle = heappop(states)[3]
        zero_idxs = puzzle.get_next_zero_index()
        for zero_idx in zero_idxs:
            new = deepcopy(puzzle)
            new.move_zero_to(zero_idx)
            dec = new.get_dec()
            if dec == answer_dec:
                return new.count
            if index(history, dec) == -1:
                heappush(states, (new.cost, new.count, dec, new))
                insort_left(history, dec)
        del puzzle


def main():
    state = []
    for _ in range(4):
        line = input().split()
        line = list(map(int, line))
        state.extend(line)
    print(solve_puzzle(state))


if __name__ == "__main__":
    main()


# from heapq import heappop, heappush
# from copy import deepcopy
# from bisect import bisect_left, insort_left


# next_zero_idx = ((1, 4), (0, 2, 5), (1, 3, 6), (2, 7),
#                  (0, 5, 8), (1, 4, 6, 9), (2, 5, 7, 10), (3, 6, 11),
#                  (4, 9, 12), (5, 8, 10, 13), (6, 9, 11, 14), (7, 10, 15),
#                  (8, 13), (9, 12, 14), (10, 13, 15), (11, 14))
# answer_idx = [15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# idx22d = ((0, 0), (0, 1), (0, 2), (0, 3),
#           (1, 0), (1, 1), (1, 2), (1, 3),
#           (2, 0), (2, 1), (2, 2), (2, 3),
#           (3, 0), (3, 1), (3, 2), (3, 3))
# manhattan = [[0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4, 5, 3, 4, 5, 6],
#              [1, 0, 1, 2, 2, 1, 2, 3, 3, 2, 3, 4, 4, 3, 4, 5],
#              [2, 1, 0, 1, 3, 2, 1, 2, 4, 3, 2, 3, 5, 4, 3, 4],
#              [3, 2, 1, 0, 4, 3, 2, 1, 5, 4, 3, 2, 6, 5, 4, 3],
#              [1, 2, 3, 4, 0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4, 5],
#              [2, 1, 2, 3, 1, 0, 1, 2, 2, 1, 2, 3, 3, 2, 3, 4],
#              [3, 2, 1, 2, 2, 1, 0, 1, 3, 2, 1, 2, 4, 3, 2, 3],
#              [4, 3, 2, 1, 3, 2, 1, 0, 4, 3, 2, 1, 5, 4, 3, 2],
#              [2, 3, 4, 5, 1, 2, 3, 4, 0, 1, 2, 3, 1, 2, 3, 4],
#              [3, 2, 3, 4, 2, 1, 2, 3, 1, 0, 1, 2, 2, 1, 2, 3],
#              [4, 3, 2, 3, 3, 2, 1, 2, 2, 1, 0, 1, 3, 2, 1, 2],
#              [5, 4, 3, 2, 4, 3, 2, 1, 3, 2, 1, 0, 4, 3, 2, 1],
#              [3, 4, 5, 6, 2, 3, 4, 5, 1, 2, 3, 4, 0, 1, 2, 3],
#              [4, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3, 1, 0, 1, 2],
#              [5, 4, 3, 4, 4, 3, 2, 3, 3, 2, 1, 2, 2, 1, 0, 1],
#              [6, 5, 4, 3, 5, 4, 3, 2, 4, 3, 2, 1, 3, 2, 1, 0]]
# manhattan = tuple(tuple(x) for x in manhattan)


# class Puzzle():
#     def __init__(self, state, count=0):
#         self.next_zero_idx = next_zero_idx
#         self.answer_idx = answer_idx
#         self.idx22d = idx22d
#         self.manhattan = manhattan
#         self.state = state
#         self.number_idx = self.get_number_idx(state)
#         self.count = count
#         self.cost = self.count + self.calc_manhattan()
#         self.prev_zero_idx = self.number_idx[0]

#     def get_number_idx(self, state):
#         number_idx = [state.index(i) for i in range(16)]
#         return number_idx

#     def calc_manhattan(self):
#         manhattan_sum = 0
#         for i in range(16):
#             manhattan_sum += manhattan[self.number_idx[i]][self.answer_idx[i]]
#         return manhattan_sum

#     def get_next_zero_index(self):
#         i = self.number_idx[0]
#         for next_zero_idx in self.next_zero_idx[i]:
#             if next_zero_idx != self.prev_zero_idx:
#                 yield next_zero_idx

#     def move_zero_to(self, idx):
#         zero_i = self.number_idx[0]
#         target_i = idx
#         target = self.state[target_i]
#         self.state[zero_i], self.state[target_i] = target, 0
#         self.number_idx[0], self.number_idx[target] = target_i, zero_i
#         self.prev_zero_idx = zero_i
#         self.count += 1
#         self.cost = self.count + self.calc_manhattan()

#     def is_answer(self):
#         return self.number_idx == self.answer_idx

#     def print_state(self):
#         for i in range(4):
#             print(" ".join(list(map(str, self.state[i * 4:i * 4 + 4]))))

#     def __eq__(self, other):
#         return self.state == other.state

#     def get_dec(self):
#         dec = 0
#         for i in range(16):
#             dec += self.state[i] * (16 ** i)
#         return dec


# def solve_puzzle(state):
#     init = Puzzle(state)
#     if init.is_answer():
#         return 0

#     states = []
#     history = []

#     def index(lst, val):
#         idx = bisect_left(lst, val)
#         if idx < len(lst) and lst[idx] == val:
#             return idx
#         return -1
#     dec = init.get_dec()
#     heappush(states, (init.cost, init.count, dec, init))
#     insort_left(history, dec)

#     while True:
#         _, _, _, puzzle = heappop(states)
#         zero_idxs = puzzle.get_next_zero_index()
#         for zero_idx in zero_idxs:
#             new = deepcopy(puzzle)
#             new.move_zero_to(zero_idx)
#             dec = new.get_dec()
#             if new.is_answer():
#                 return new.count
#             if index(history, dec) == -1:
#                 heappush(states, (new.cost, new.count, dec, new))
#                 insort_left(history, dec)
#         del puzzle


# def main():
#     state = []
#     for _ in range(4):
#         line = input().split()
#         line = list(map(int, line))
#         state.extend(line)
#     print(solve_puzzle(state))


# if __name__ == "__main__":
#     main()
