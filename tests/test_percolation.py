import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from percolation import percolates, lower_bound_L


def test_d4_even_parity():
    evens = [v for v in range(16) if bin(v).count("1") % 2 == 0]
    assert percolates(evens, 4, 4) is True
    assert len(evens) == 8


def test_d4_optimum_set():
    s = [0, 3, 5, 6, 9, 10, 12, 15]
    assert percolates(s, 4, 4) is True


def test_d5_verified_set():
    s = [2, 5, 7, 8, 11, 13, 14, 16, 19, 21, 22, 25, 26, 28]
    assert percolates(s, 5, 4) is True
    assert len(s) == 14


def test_d6_verified_set():
    s = [0, 3, 5, 6, 10, 20, 23, 24, 27, 29, 33, 43, 45, 46, 51, 54, 58, 60]
    assert percolates(s, 6, 4) is True
    assert len(s) == 18


def test_lower_bound_values():
    # L(4)=8, L(6)=18 exactly; L(5)=12.25
    assert abs(lower_bound_L(4) - 8.0) < 1e-9
    assert abs(lower_bound_L(6) - 18.0) < 1e-9
    assert abs(lower_bound_L(5) - 12.25) < 1e-9
