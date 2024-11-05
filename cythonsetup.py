
from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "cppheader",                  
        sources=["cppheader.pyx", "cppheader.cpp"],
        language="c++",
        extra_compile_args=["-O3"],    
    )
]

setup(
    name="cppheader",
    ext_modules=cythonize(ext_modules),
)
