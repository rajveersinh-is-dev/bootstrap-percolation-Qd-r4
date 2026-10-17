from ortools.sat.python import cp_model
import itertools

def solve_min(d, r, time_limit=120):
    n = 1<<d
    # neighbors
    nbrs = [[] for _ in range(n)]
    for v in range(n):
        for i in range(d):
            nbrs[v].append(v ^ (1<<i))
    model = cp_model.CpModel()
    z = [model.NewBoolVar(f'z_{v}') for v in range(n)]
    t = [model.NewIntVar(0, n, f't_{v}') for v in range(n)]
    # z=1 => t=0
    for v in range(n):
        model.Add(t[v] <= (1 - z[v]) * n)
        model.Add(t[v] >= 1 - z[v])
    # le variables
    le = {}
    for v in range(n):
        for u in nbrs[v]:
            key = (u,v)
            if key not in le:
                b = model.NewBoolVar(f'le_{u}_{v}')
                le[key]=b
                # b => t[u] + 1 <= t[v]
                model.Add(t[u] + 1 <= t[v]).OnlyEnforceIf(b)
                model.Add(t[u] >= t[v]).OnlyEnforceIf(b.Not())
    # count constraint
    for v in range(n):
        s = sum(le[(u,v)] for u in nbrs[v])
        # if z[v]=0 need s>=r
        model.Add(s >= r).OnlyEnforceIf(z[v].Not())
    model.Minimize(sum(z))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = 8
    status = solver.Solve(model)
    print("status", solver.StatusName(status))
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        k = int(solver.ObjectiveValue())
        init = [v for v in range(n) if solver.Value(z[v])==1]
        print("k", k, "init", init)
        return k, init
    return None

for d in [7]:
    print("=== d",d)
    solve_min(d,4, time_limit=580)
