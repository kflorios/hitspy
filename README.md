# hitspy

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**hitspy** is a high-performance Python package providing C++ implementation of discrete Tabu Search algorithm for maximum score estimation. Powered by **pybind11** and parallelized with **OpenMP**, `hitspy` accelerates Hyperplanes Intersection evaluation and search routines across large search spaces.

---

## Key Features

- ⚡ **High Performance**: Core optimization routines written in C++ for maximum throughput.
- 🚀 **Parallel Computing**: OpenMP multi-threading support for fast neighborhood evaluations.
- 🐍 **Seamless Python API**: Native `numpy` array integration using `pybind11`.

---

## Installation

### From Source (Locally)

Download the main folder of the package, cd to it and provide
in your preferred environment:

```bash
pip install -e .
```
---

### Requirements
Python 3.8 and above, MS Visual Studio 2019 and above

## API Reference

### `hitspy.run_tabu_search`

Executes an OpenMP-accelerated discrete Tabu Search algorithm for maximum score estimator computation.

```python
hitspy.run_tabu_search(
    X: numpy.ndarray,
    y: numpy.ndarray,
    b0: float,
    d: float,
    iSeed: int
) -> numpy.ndarray
```

## Complete Example: Multi-Seed Benchmark (20 Random Starts)

This benchmark demonstrates how to execute 20 distinct random restarts using `hitspy`, summarize overall solution quality, and compute selection frequency statistics for each attribute.

```python
import numpy as np
import pandas as pd
from hitspy import run_tabu_search

# 1. Load and preprocess data
X_raw = np.loadtxt("X.txt")
y_raw = np.loadtxt("y.txt")

X = X_raw[:, 1:]
y = y_raw[:, 1].astype(int)
X=np.transpose(X)
X = np.ascontiguousarray(X, dtype=np.float64)

# 2. Parameters
b0 = -1.0
d = 10000
num_runs = 20

# Generate 20 distinct random seeds
np.random.seed(42)  # For reproducible seed generation
seeds = np.random.randint(0, 1000000, size=num_runs)

# 3. Storage for results
results_list = []

print("Starting 20 runs...")

# 4. Run loop
for i in range(num_runs):
    print('run...:',i+1)
    current_seed = int(seeds[i])

    # Execute Tabu Search
    attrs, coeffs, score = run_tabu_search(X=X, y=y, b0=b0, d=d, iSeed=current_seed)

    # hitspy returns results in attrs, coeffs, score

    # Save metrics
    results_list.append(
        {
            "Run": i + 1,
            "Seed": current_seed,
            "Score": score,
            "Coeffs": coeffs,
            "Attrs": attrs
        }
    )

# 5. Combine into a single DataFrame
results_df = pd.DataFrame(results_list)

# 6. Display results table
print(results_df.to_string(index=False))

# 7. Summary statistics
print("\n=== Summary Across 20 Runs ===")
print("Best Score Found: ", results_df["Score"].max())
print("Mean Score:       ", results_df["Score"].mean())
print("Score Std Dev:    ", results_df["Score"].std(ddof=1))
```

## Acknowledgements 

I would like to thank Dr. **Alexandros Louka** and Professor **Yannis Bilias** for their valuable help and the shared ideas for the development of HITSpy. The development of the HITSpy software was supported by the Hellenic Foundation for Research and Innovation (H.F.R.I.) under the '2nd Call for H.F.R.I. Research Projects to support Post-Doctoral Researchers' (Project Number: 902). 

## Citation

If you use `hitspy` in your research, please cite the underlying methodology papers:

```bibtex
@article{florios2025hits,
  title={HITS: Hyperplanes intersection tabu search for maximum score estimation},
  author={Florios, Kostas and Louka, Alexandros and Bilias, Yannis},
  journal={SoftwareX},
  volume={30},
  pages={102164},
  year={2025},
  publisher={Elsevier}
}

@article{manski1975maximum,
  title={Maximum score estimation of the stochastic utility model of choice},
  author={Manski, Charles F},
  journal={Journal of econometrics},
  volume={3},
  number={3},
  pages={205--228},
  year={1975},
  publisher={Elsevier}
}
