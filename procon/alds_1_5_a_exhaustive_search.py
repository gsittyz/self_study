def main():
    def can_make_sum(index, goal):
        # index以降のcandidatesを足し合わせてgoalをつくれる
        if index >= n:
            return False
        if goal == candidates[index]:
            return True
        else:
            # 使わないで目標値に行くか、使って目標値に行く
            return can_make_sum(index + 1, goal) | can_make_sum(index + 1, goal - candidates[index])
    n = int(input())
    candidates = list(map(int, input().split(" ")))
    input()
    goals = list(map(int, input().split(" ")))
    for goal in goals:
        print(["no", "yes"][can_make_sum(0, goal) * 1])


if __name__ == "__main__":
    main()
