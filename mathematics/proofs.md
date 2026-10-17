# Proofs

## Lower bound

See Morrison–Noel (2017), Theorem 1.3, with $r=4$. The proof uses weak saturation: $m(G,r)\ge \operatorname{wsat}(G,S_{r+1})/r$, and an exact expression for $\operatorname{wsat}(Q_d,S_{r+1})$. We do not reprove it here; the repository cites the source and reproduces the simplified expression $L(d)$.

## Upper bound / constructions

- $d=4$: the even-parity vertex set? No—verified optimum $8$ equals the set of even-parity vertices, which percolates because every odd vertex has all four neighbours even. Size $2^{3}=8$.
- $d=5$: a 14-element percolating set found by CP-SAT (listed in `results/small_cases.md`). Optimality proved by the solver (optimal status).
- $d=6$: an 18-element set found by CP-SAT matching the lower bound; optimality follows from the lower bound.

## Verification of percolation

All sets were checked by the independent simulator in `src/percolation.py` (deterministic closure under the $4$-neighbour rule). See `tests/test_percolation.py`.
