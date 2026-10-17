# Known Results

## Theorem (Morrison–Noel lower bound, $r=4$)

For every $d\ge 4$,

\[
m(Q_d,4)\ge L(d):=\frac{d(d^2+3d+14)}{24}+1.
\]

In particular, since $m$ is integer, $m(Q_d,4)\ge \lceil L(d)\rceil$.

## Constructions

- **Even-parity construction (general).** The set of all vertices of $Q_d$ of even parity has size $2^{d-1}$. For $r=d$ (threshold equal to degree) this percolates; for $r=4<d$ it is not minimal. Not used for $r=4$.
- **Noel's construction.** For $d$ with $d+1\equiv 2$ or $4\pmod 6$, a percolating set of size exactly $L(d)$ exists. For general $d$, a percolating set of size $L(d)+O(d)$ exists.

## Verified small cases (this project)

Computed by exact CP-SAT optimisation (OR-Tools) for threshold $4$:

| $d$ | $n=2^d$ | $\lceil L(d)\rceil$ | $m(Q_d,4)$ (verified) | gap |
|---|---|---|---|---|
| 4 | 16 | 8 | 8 | 0 |
| 5 | 32 | 13 | 14 | 1 |
| 6 | 64 | 18 | 18 | 0 |
| 7 | 128 | 26 | pending | — |

The verified cases show the gap is not uniformly zero; the exact value depends on $d$ in a way not captured by $\lceil L(d)\rceil$ alone.
