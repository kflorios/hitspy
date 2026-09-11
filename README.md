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
Python 3.8 and above, MSVStudio 2019 and above

## Acknowledgements 

I would like to thank Dr. **Alexandros Louka** and Professor **Yannis Bilias** for their valuable help and the shared ideas for the development of HITSr. The development of the HITSr software was supported by the Hellenic Foundation for Research and Innovation (H.F.R.I.) under the '2nd Call for H.F.R.I. Research Projects to support Post-Doctoral Researchers' (Project Number: 902). 

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
