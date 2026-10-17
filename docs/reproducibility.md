# Reproducibility

## Environment

- Python 3.14.6
- OR-Tools 9.15.6755 (CP-SAT)
- networkx 3.6.1

## Run tests

```powershell
python -m pytest tests/ -q
```

## Reproduce small-case optima

```powershell
python solve_bp.py   # edit d in solve_bp.py; may take several minutes for d>=6
```

The CP-SAT model is in `solve_bp.py`. It encodes infection times and the $r$-neighbour condition, minimises the number of initially infected vertices, and reports optimal/feasible status.

## Verify a set percolates

```python
from src.percolation import percolates
percolates([0,3,5,6,9,10,12,15], 4, 4)  # True
```
