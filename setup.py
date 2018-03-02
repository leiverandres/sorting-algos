from Cython.Build import cythonize
from distutils.core import setup

setup(
    name='Sorting app',
    ext_modules=cythonize("cocktailsort.pyx"),
)