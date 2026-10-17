"""Module for mathematical computation and analysis."""

from __future__ import annotations

import itertools


def neighbors(v, d):
    """Neighbors.
    
    Args:
        v:
        d:
    
    """
    for i in range(d):
        yield v ^ (1<<i)


def percolates(initial, d):
    """Percolates.
    
    Args:
        initial:
        d:
    
    Returns:
        The computed result
    
    """
    n = 1<<d
    infected = set(initial)
    changed = True
    while changed:
        changed = False
        for v in range(n):
            if v in infected:
                continue
            cnt = sum(1 for u in neighbors(v,d) if u in infected)
            if cnt >= 4:  # threshold 4 (but should be general r)
                infected.add(v); changed=True
    return len(infected)==n


def min_perc(d, r) -> tuple:
    """Min perc.
    
    Args:
        d:
        r:
    
    Returns:
        tuple: Result of type tuple
    
    """
    n = 1<<d
    # threshold r
    def perc(initial):
        """Perc.
        
        Args:
            initial:
        
        Returns:
            The computed result
        
        """
        infected=set(initial); changed=True
        while changed:
            changed=False
            for v in range(n):
                if v in infected:
                    continue
                cnt=sum(1 for u in neighbors(v,d) if u in infected)
                if cnt>=r:
                    infected.add(v); changed=True
        return len(infected)==n
    for k in range(1, n+1):
        for combo in itertools.combinations(range(n), k):
            if perc(combo):
                return k, combo
    return None

for d in [4]:
    print("d",d)
    k,combo = min_perc(d,4)
    print("min k", k, "combo", combo)
    L = d*(d*d+3*d+14)//24 + 1
    print("L(d)", L)
