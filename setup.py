from setuptools import setup, find_packages

setup(
    name="legend200-detector-mapper",
    version="0.1.0",
    description="A tool for mapping and inspecting LEGEND HPGe detectors.",
    author="Marta Babicz",
    author_email="marta.babicz@physik.uzh.ch",
    packages=find_packages(),
    install_requires=[
        "awkward",
        "matplotlib",
        "legendmeta",
        "lgdo",
        "h5py",
        "pandas",
        "ipywidgets",
    ],
    python_requires=">=3.6",
)
