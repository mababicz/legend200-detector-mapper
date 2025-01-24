from setuptools import setup, find_packages

setup(
    name="legend200-detector-mapper",
    version="0.1.0",
    description="Tool to map LEGEND HPGe detectors and analyze their statuses.",
    author="Dr. Marta Babicz",
    author_email="marta.babicz@physik.uzh.ch",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
    ],
    python_requires=">=3.6",
)

