# Bootstrap Percolation in $Q_d$: Exact Minimum Percolating Sets for Threshold $4$

## Problem

Determine $m(Q_d,4)$: the minimum size of an initial set that percolates in the $d$-dimensional hypercube under $4$-neighbour bootstrap percolation.

## Strongest result obtained

- Lower bound $m(Q_d,4)\ge L(d)=d(d^2+3d+14)/24+1$ (Morrison--Noel, reproduced).
- Exact values verified for $d=4,5,6$: $8,14,18$.
- The gap $m-\lceil L\rceil$ is $0,1,0$ for $d=4,5,6$; its general behaviour is an open question.

## Repository map

- `research/` — problem selection, literature, known results, proof attempts.
- `mathematics/` — definitions, main results, proofs.
- `paper/main.tex` — paper draft.
- `src/percolation.py` — simulator.
- `tests/test_percolation.py` — tests.
- `experiments/`, `results/` — computation and verified sets.
- `docs/reproducibility.md` — reproduction instructions.

## Reproduce

```powershell
python -m pytest tests/ -q
```

## Limitations

The gap pattern is not proved; $d=7$ computation was in progress at publication. The lower bound is prior work.

## License

MIT.
