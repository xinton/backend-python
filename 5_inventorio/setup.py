from setuptools import setup, find_packages

setup(
    name="inventorio",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer>=0.9.0",
        "pytest>=7.0.0",
    ],
    entry_points={
        "console_scripts": [
            "inventorio=inventorio.cli:main",
        ],
    },
)