from setuptools import setup, Extension
import pybind11

module = Extension(
    'libsyncro',  # Name of the extension module
    sources=['syncro.cpp'],  # Your C++ source file
    include_dirs=[pybind11.get_include()],  # Path to pybind11 headers
    language='c++',
)

setup(
    name='libsyncro',
    ext_modules=[module],
)
