def solution(ineq, eq, n, m):
    if eq == "=":
        if ineq == "<":
            return int(bool(n <= m))
        else:
            return int(bool(n >= m))
    elif eq == "!":
        if ineq == "<":
            return int(bool(n < m))
        else:
            return int(bool(n > m))