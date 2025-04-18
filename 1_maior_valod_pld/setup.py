from setuptools import setup, find_packages

setup(
    name="pld_analyzer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.5.0",
        "openpyxl>=3.0.0",
        "pytest>=7.0.0",
    ],
)