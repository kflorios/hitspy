#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include "tabu_search.hpp"

extern "C" int run_tabu_search(
    double* X,
    int T,
    int p_in,
    int* y_in,
    double b0,
    int d,
    int iSeed,                 // <-- NEW ARGUMENT
    int* out_attributes,
    double* out_coeffs,
    double* out_score
);

namespace py = pybind11;

py::tuple py_run_tabu_search(py::array_t<double> X,
                             py::array_t<int> y,
                             double b0,
                             int d,
                             int iSeed)
{
    if (X.ndim() != 2)
        throw std::runtime_error("X must be 2D (p_in x T)");
    if (y.ndim() != 1)
        throw std::runtime_error("y must be 1D (T,)");

    int p_in = static_cast<int>(X.shape(0));
    int T    = static_cast<int>(X.shape(1));

    if (y.shape(0) != T)
        throw std::runtime_error("y length must match X.shape[1]");

    auto X_buf = X.request();
    auto y_buf = y.request();

    double* X_ptr = static_cast<double*>(X_buf.ptr);
    int*    y_ptr = static_cast<int*>(y_buf.ptr);

    int p = p_in - 1;
    if (p <= 0 || p > pmax)
        throw std::runtime_error("p_in-1 must be in [1, pmax]");

    py::array_t<int>    attrs({p});
    py::array_t<double> coeffs({p});
    double score = 0.0;

    auto attrs_buf   = attrs.request();
    auto coeffs_buf  = coeffs.request();

    int*    attrs_ptr  = static_cast<int*>(attrs_buf.ptr);
    double* coeffs_ptr = static_cast<double*>(coeffs_buf.ptr);

int ret = run_tabu_search(
    X_ptr,
    T,
    p_in,
    y_ptr,
    b0,
    d,
    iSeed,                 // <-- pass seed
    attrs_ptr,
    coeffs_ptr,
    &score
);

    if (ret != 0)
        throw std::runtime_error("run_tabu_search failed with code " + std::to_string(ret));

    return py::make_tuple(attrs, coeffs, score);
}

PYBIND11_MODULE(_hitspy, m) {
    m.doc() = "Pybind11 bindings for hitspy discrete tabu search";

    m.def("run_tabu_search", &py_run_tabu_search,
          py::arg("X"),
          py::arg("y"),
          py::arg("b0"),
          py::arg("d"),
          py::arg("iSeed"),
          "Run discrete tabu search with user-specified RNG seed.");
}
