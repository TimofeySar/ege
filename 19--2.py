def f(s, m):
    if s >= 62: return m%2==0
    elif m <= 0: return 0
    h = [f(s + 1, m-1), f(s *2, m-1)]
    if m%2 != 0:
        return any(h)
    return all(h)

print('19', [s for s in range(1, 62) if (not(f(s, 2))) and f(s, 4)])