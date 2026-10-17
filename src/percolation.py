"""Hypercube bootstrap percolation utilities."""
from __future__ import annotations




def vertices(d) -> list:
    """Vertices.
    
    Args:
        d:
    
    Returns:
        list: Result of type list
    
    """
    return list(range(1 << d))


def neighbors(v, d):
    """Neighbors.
    
    Args:
        v:
        d:
    
    """
    for i in range(d):
        yield v ^ (1 << i)


def percolates(initial, d, r=4):
    """Return True iff the initial set percolates in Q_d under r-neighbour rule."""
    n = 1 << d
    infected = set(initial)
    changed = True
    while changed:
        changed = False
        for v in range(n):
            if v in infected:
                continue
            cnt = sum(1 for u in neighbors(v, d) if u in infected)
            if cnt >= r:
                infected.add(v)
                changed = True
    return len(infected) == n


def closure(initial, d, r=4):
    """Closure.
    
    Args:
        initial:
        d:
        r (int):
    
    Returns:
        The computed result
    
    """
    n = 1 << d
    infected = set(initial)
    changed = True
    while changed:
        changed = False
        for v in range(n):
            if v in infected:
                continue
            cnt = sum(1 for u in neighbors(v, d) if u in infected)
            if cnt >= r:
                infected.add(v)
                changed = True
    return infected


def lower_bound_L(d):
    """Morrison-Noel lower bound value L(d) (may be fractional)."""
    return d * (d * d + 3 * d + 14) / 24.0 + 1.0


if __name__ == "__main__":
    # smoke test
    d = 4
    init = list(range(0, 1 << d, 2))  # even? not exactly; use parity
    evens = [v for v in range(1 << d) if bin(v).count("1") % 2 == 0]
    print("d=4 even parity percolates:", percolates(evens, 4, 4))
