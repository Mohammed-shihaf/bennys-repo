# minilab -- PY_V312_MINIMAL

A minimal Python 3.12 white-box fixture. Three things, one file each, nothing else:

| Area | File | What it is for |
|---|---|---|
| Static analysis | `src/minilab/static_fixture.py` | planted lint, security, dead-code and complexity findings |
| Coverage | `src/minilab/refunds.py` + `tests/test_coverage_partial.py` | branches deliberately left untested |
| Test techniques | `src/minilab/pricing.py` + three `tests/test_*.py` | equivalence partitioning, boundary values, decision table |

No services, no build backend, no tool runners. `pip install -r requirements.txt` and go.

## Run

```
python -m pytest
python -m coverage run -m pytest && python -m coverage report -m
python -m ruff check src/minilab
python -m radon cc src/minilab -s
python -m bandit -r src/minilab
python -m vulture src/minilab --min-confidence 80
```

## Expected results

Measured on CPython 3.12.11 with the pins in `requirements.txt`.

### Tests: 25 pass

| File | Technique | Tests |
|---|---|---|
| `test_equivalence_partitioning.py` | one representative per tier class (3 valid, 1 invalid) | 4 |
| `test_boundary_values.py` | just below and on each step at 25 / 100 / 500, negative input, the 0.15 cap | 9 |
| `test_decision_table.py` | all 8 rules of `shipping_fee(express, heavy, member)` | 8 |
| `test_coverage_partial.py` | partial on purpose | 4 |

### Coverage: 87% total (branch coverage on)

| File | Stmts | Miss | Branch | BrPart | Cover | Missing |
|---|---|---|---|---|---|---|
| `pricing.py` | 28 | 0 | 16 | 0 | 100% | |
| `refunds.py` | 16 | 5 | 10 | 2 | 65% | 13, 18, 27-29 |

`static_fixture.py` is omitted in `pyproject.toml`; with it included the total drops,
because nothing imports it. Line-only coverage (no `--branch`) of `refunds.py` is 11/16 = 69%.

### Static analysis, all in `static_fixture.py`

| Tool | Expected |
|---|---|
| ruff | 10 findings: F401, S105, N802, B006, F841, E722, S110, S602, S307, S324 |
| bandit | 6 findings: B404, B105, B110 (low), B307 (medium), B602, B324 (high) |
| radon / lizard | `classify` is CC 14 (rank C), the only function over 10; next highest is `shipping_fee` at 7 |
| vulture | at 80% confidence: unused import `json` (line 8), unreachable code (line 43) |

`pricing.py` and `refunds.py` are clean under ruff and bandit. Below 80% confidence vulture also
lists every public function, since nothing but the tests calls them.
