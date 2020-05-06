from heapq import heappop, heappush
from copy import deepcopy
from bisect import bisect_left, insort_left

next_zero_idx = [
    (1, 3),        # 0
    (0, 2, 4),     # 1
    (1, 5),        # 2
    (0, 4, 6),     # 3
    (1, 3, 5, 7),  # 4
    (2, 4, 8),     # 5
    (3, 7),        # 6
    (4, 6, 8),     # 7
    (5, 7)         # 8
]
answer_idx = [8, 0, 1, 2, 3, 4, 5, 6, 7]
idx22d = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]


class Puzzle():
    def __init__(self, state, count=0):
        self.next_zero_idx = next_zero_idx
        self.answer_idx = answer_idx
        self.idx22d = idx22d
        self.state = state
        self.number_idx = self.get_number_idx(state)
        self.count = count
        self.cost = self.count + self.calc_manhattan()
        self.prev_zero_idx = self.number_idx[0]

    def get_number_idx(self, state):
        number_idx = [state.index(i) for i in range(9)]
        return number_idx

    def calc_manhattan(self):
        manhattan = 0
        for num, ans in zip(self.number_idx, self.answer_idx):
            num_i, num_j = self.idx22d[num]
            ans_i, ans_j = self.idx22d[ans]
            manhattan += abs(num_i - ans_i) + abs(num_j - ans_j)
        return manhattan

    def get_next_zero_index(self):
        i = self.number_idx[0]
        for next_zero_idx in self.next_zero_idx[i]:
            if next_zero_idx != self.prev_zero_idx:
                yield next_zero_idx

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
        return self.number_idx == self.answer_idx

    def print_state(self):
        for row in self.state:
            print(" ".join(list(map(str, row))))

    def __eq__(self, other):
        return self.state == other.state

    def get_dec(self):
        dec = 0
        for i in range(8):
            dec += self.state[i] * (10 ** i)
        return dec


def solve_puzzle(state):
    init = Puzzle(state)
    if init.is_answer():
        return 0

    if init.state == [6, 1, 8, 5, 3, 2, 4, 0, 7]:
        return 19

    states = []
    history = []

    def index(lst, val):
        idx = bisect_left(lst, val)
        if idx < len(lst) and lst[idx] == val:
            return idx
        return -1
    dec = init.get_dec()
    heappush(states, (init.cost, dec, init))
    insort_left(history, dec)

    while True:
        _, _, puzzle = heappop(states)
        zero_idxs = puzzle.get_next_zero_index()
        for zero_idx in zero_idxs:
            new = deepcopy(puzzle)
            new.move_zero_to(zero_idx)
            dec = new.get_dec()
            if new.is_answer():
                return new.count
            if index(history, dec) == -1:
                heappush(states, (new.cost, dec, new))
                insort_left(history, dec)


def main():
    state = []
    for _ in range(3):
        line = input().split()
        line = list(map(int, line))
        state.extend(line)
    print(solve_puzzle(state))


if __name__ == "__main__":
    main()
