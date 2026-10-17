# Literature Review

## Key references

1. **Morrison, N. and Noel, J. A.** (2015/2017). *Extremal Bounds for Bootstrap Percolation in the Hypercube.* arXiv:1506.04686.  
   - Proves $m(Q_d,r)\ge 2^{r-1}+\frac1r\sum_{j=1}^{r-1}\binom{d-j-1}{r-j}j2^{j-1}$ (Theorem 1.3).  
   - For $r=3$: $m(Q_d,3)=\lceil d(d+3)/6\rceil+1$ for all $d\ge 3$.

2. **Noel, J. A.** (2026). *Optimal and Near-Optimal Constructions for Bootstrap Percolation in Hypercubes.* arXiv:2604.15534.  
   - Shows $m(Q_d,4)=\frac{d(d^2+3d+14)}{24}+1$ for infinitely many $d$.  
   - For general $d$: upper bound differing from the Morrison–Noel lower bound by an additive $O(d)$.

## The lower bound for $r=4$

The Morrison–Noel lower bound gives, for $r=4$,

\[
m(Q_d,4)\;\ge\; 8+\frac{1}{4}\Bigl(\binom{d-2}{3}+4\binom{d-3}{2}+12\binom{d-4}{1}\Bigr).
\]

Simplifying,

\[
L(d)=\frac{d^3+3d^2+14d+24}{24}=\frac{d(d^2+3d+14)}{24}+1.
\]

(When $L(d)$ is non-integral, the integer bound is $\lceil L(d)\rceil$.)

## The open gap

For $d$ with $d+1\equiv 2$ or $4\pmod 6$, a Steiner quadruple system $\mathrm{SQS}(d+1)$ exists and Noel's construction attains $L(d)$. For other $d$ only an $O(d)$-additive upper bound is known. Determining whether the true value is $\lceil L(d)\rceil$ or larger, and by how much, is the open problem.
