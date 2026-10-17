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

## Conjecture (pattern of the gap)

Let $g(d)=m(Q_d,4)-\lceil L(d)\rceil$. From the verified cases $g(4)=0$, $g(5)=1$, $g(6)=0$. We conjecture $g(d)\in\{0,1\}$ and $g(d)=1$ iff $d\equiv 1$ or $5\pmod 6$? (Equivalently, iff $d+1\not\equiv 2,4\pmod 6$, i.e. no Steiner quadruple system $\mathrm{SQS}(d+1)$.) This is consistent with Noel's construction attaining $L(d)$ exactly when an SQS$(d+1)$ exists, and with the $d=5$ case (where no SQS$(6)$ exists) having gap $1$.

*Status: CONJECTURED. Not proved. Requires verification for further $d$ and a construction proving the upper bound for the gap-$1$ cases.*
