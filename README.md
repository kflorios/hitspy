# hitspy

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**hitspy** is a high-performance Python package providing C++ implementations of discrete Tabu Search algorithm for maximum score estimation. Powered by **pybind11** and parallelized with **OpenMP**, `hitspy` accelerates Hyperplanes Intersection evaluation and search routines across large search spaces.

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
