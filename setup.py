from setuptools import setup, find_packages

setup(
    name="MyProject",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "pytest-cov",
        "flake8",
        "black",
    ],
)