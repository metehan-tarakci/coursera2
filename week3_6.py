#linear

def count_subpeptides(n):
    return ((n * (n + 1)) // 2) + 1

# Example Input
n = 28407

print(count_subpeptides(n))