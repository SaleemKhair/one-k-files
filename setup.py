from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="one-k-files",
    version="0.0.1",
    description="tamatem plus assignment",
    url="https://github.com/SaleemKhair/one-k-files",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    entry_points={ 
        "console_scripts": [
            "one_k_files=one_k_files:main",
        ],
    },
)
