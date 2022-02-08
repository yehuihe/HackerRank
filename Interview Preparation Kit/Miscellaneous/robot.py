def solution(R):
    N = len(R)
    M = len(R[0])

    # Generate grid
    grid = {}
    for i in range(N):
        for j in range(M):
            grid[(i, j)] = "X" if R[i][j] == "X" else 0

    # Initiate (0, 0) grid
    grid[(0, 0)] = 1

    steps = 0
    max_steps = 1000
    # Current grid position
    i = j = 0
    # Current moving direction
    right = True
    down = False
    left = False
    up = False
    while steps < max_steps:
        if right:
            if j == M - 1 or grid[(i, j + 1)] == "X":
                right = False
                down = True
            else:
                j += 1
        elif down:
            if i == N - 1 or grid[(i + 1, j)] == "X":
                down = False
                left = True
            else:
                i += 1
        elif left:
            if j == 0 or grid[(i, j - 1)] == "X":
                left = False
                up = True
            else:
                j -= 1
        elif up:
            if i == 0 or grid[(i - 1, j)] == "X":
                up = False
                right = True
            else:
                i -= 1

        # Recording position (i, j) in each iteration
        grid[(i, j)] += 1
        steps += 1

    count = 0
    for v in grid.values():
        if v != 0 and v != "X":
            count += 1

    return count


if __name__ == "__main__":

    A = [
        "....X...",
        "........",
        "........",
        "..X.....",
        "........",
        "........",
        ".X......",
    ]  # Answer: 22
    print(solution(A))
