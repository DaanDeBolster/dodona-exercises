def harmonisch(n):
    if n == 1:
        return 1.0
    else:
        return harmonisch(n-1)+1/n