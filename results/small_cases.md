# Verified small cases: $m(Q_d,4)$

Computed by exact CP-SAT (OR-Tools) for threshold $r=4$.

## $d=4$ ($n=16$)

- Minimum: $8$.
- Set: $\{0,3,5,6,9,10,12,15\}$ (all even-parity vertices).
- Lower bound $\lceil L(4)\rceil=8$. Gap $0$.

## $d=5$ ($n=32$)

- Minimum: $14$ (proved optimal by solver).
- Set: $\{2,5,7,8,11,13,14,16,19,21,22,25,26,28\}$.
- Lower bound $\lceil L(5)\rceil=13$. Gap $1$.

## $d=6$ ($n=64$)

- Feasible set of size $18$ matching the lower bound: $\{0,3,5,6,10,20,23,24,27,29,33,43,45,46,51,54,58,60\}$.
- Lower bound $\lceil L(6)\rceil=18$. Gap $0$ (optimality by lower bound).

## $d=7$ ($n=128$)

- Feasible set of size $26$ matching the lower bound: $\{6,8,13,19,21,25,30,32,37,38,43,44,49,55,58,68,73,74,92,98,104,109,110,112,115,123\}$.
- Lower bound $\lceil L(7)\rceil=26$. Gap $0$ (optimality by lower bound).
