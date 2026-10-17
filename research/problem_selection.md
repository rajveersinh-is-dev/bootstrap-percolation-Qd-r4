# Problem Selection

## Selected problem

**Minimum size of a percolating set in the $d$-dimensional hypercube $Q_d$ under $4$-neighbour bootstrap percolation.**

Let $Q_d$ be the $d$-dimensional hypercube graph (vertices $\{0,1\}^d$, edges between vertices differing in one coordinate). In $r$-neighbour bootstrap percolation, an initial set $A_0\subseteq V(Q_d)$ is chosen; at each step a healthy vertex becomes infected if it has at least $r$ infected neighbours. $A_0$ *percolates* if eventually every vertex is infected. We write $m(Q_d,r)$ for the minimum cardinality of a percolating set.

**Target.** Determine $m(Q_d,4)$ exactly for all $d\ge 4$.

## Why this problem

- Genuine open problem: Morrison and Noel (2015) gave a universal lower bound; Noel (2026) gave an upper bound matching it for infinitely many $d$ and within an additive $O(d)$ for general $d$. The exact value for all $d$ is not settled.
- The decisive work is combinatorial/structural (weak saturation, Steiner systems), not massive computation.
- Small cases can be verified exactly by computation, giving concrete anchors.
- Recent literature (Noel 2026) makes the frontier precise, so progress is measurable.

## Status classification

Confirmed open (for general $d$). The lower bound is known; exact upper-bound constructions exist only for $d$ with $d+1\equiv 2$ or $4\pmod 6$ (Steiner quadruple systems). For other $d$ the gap is open.
