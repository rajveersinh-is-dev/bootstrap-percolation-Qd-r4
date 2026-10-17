# Main Results

## Theorem (Lower bound, reproduced)

For all $d\ge 4$,

\[
m(Q_d,4)\ge \lceil L(d)\rceil,\qquad 
L(d)=\frac{d(d^2+3d+14)}{24}+1.
\]

*Status: ESTABLISHED IN PRIOR WORK (Morrison–Noel 2017). Reproduced here for completeness.*

## Proposition (Verified small cases)

By exact CP-SAT optimisation (OR-Tools, certificate of optimality for $d=4,5$; feasible matching lower bound for $d=6$):

- $m(Q_4,4)=8$.
- $m(Q_5,4)=14$.
- $m(Q_6,4)=18$.

*Status: COMPUTATIONALLY VERIFIED (finite domains, $d=4,5,6$).*

## Open question (pattern of the gap)

Let $g(d)=m(Q_d,4)-\lceil L(d)\rceil$. From the verified cases:
$g(4)=0$, $g(5)=1$, $g(6)=0$. The gap is small in these cases, but its
dependence on $d$ is not yet understood. In particular, $d=6$ has gap $0$
even though no Steiner quadruple system $\mathrm{SQS}(7)$ exists, so the
gap is not simply governed by the existence of an $\mathrm{SQS}(d+1)$.

*Status: OPEN. The values $g(d)$ for $d\ge 7$ are unknown.*
