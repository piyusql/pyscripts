def ncr(n, r):
    """Computes n! / (r! (n-r)!) exactly. Returns a python long int."""
    assert n >= 0
    assert 0 <= r <= n
    r = min(r, n - r)
    c = 1
    denom = 1
    for (num, denom) in zip(xrange(n, n - r, -1), xrange(1, r + 1, 1)):
        c = (c * num) // denom
    return c
