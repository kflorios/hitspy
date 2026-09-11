import sys
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class BuildExt(build_ext):
    """Custom build extension to handle compiler-specific flags."""
    def build_extensions(self):
        compiler = self.compiler.compiler_type
        for ext in self.extensions:
            if compiler == "msvc":
                ext.extra_compile_args = ["/O2", "/openmp", "/std:c++14"]
            else:
                ext.extra_compile_args = ["-O3", "-fopenmp", "-std=c++14"]
                ext.extra_link_args = ["-fopenmp"]
        super().build_extensions()

class get_pybind_include:
    """Helper class to delay importing pybind11 until build time."""
    def __str__(self):
        import pybind11
        return pybind11.get_include()

ext_modules = [
    Extension(
        "hitspy._hitspy",
        sources=[
            "src/hitspy/tabu_bindings.cpp",
            "src/hitspy/tabu_api.cpp",
            "src/hitspy/bsort.cpp",
            "src/hitspy/evaluate_neighbourhood.cpp",
            "src/hitspy/EvaluateScore1.cpp",
            "src/hitspy/gelim.cpp",
        ],
        include_dirs=[
            get_pybind_include(),
            "src/hitspy",
        ],
        language="c++",
    )
]

setup(
    ext_modules=ext_modules,
    cmdclass={"build_ext": BuildExt},
)