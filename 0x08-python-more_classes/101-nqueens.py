#!/usr/bin/python3
import sys

def solve(n, i, a, b, c):
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                for solution in solve(n, i+1, a+[j], b+[i+j], c+[i-j]):
                    yield solution
    else:
        yield a

def print_solution(solution):
    print("[", end="")
    for i, pos in enumerate(solution):
        print("[{}, {}]".format(i+1, pos+1), end="")
        if i != len(solution) - 1:
            print(", ", end="")
    print("]")

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    for solution in solve(n, 0, [], [], []):
        print_solution(solution)

if __name__ == "__main__":
    main()
