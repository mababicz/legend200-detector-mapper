# LEGEND200 Detector Mapper

A Python-based tool for mapping and inspecting HPGe detectors in the LEGEND200 experiment. This tool provides functionality to load metadata, filter detectors based on usability, and visualize their positions interactively.


## **Features**
- **Interactive Jupyter Notebook**: Filter detectors by usability and visualize their positions.
- **Metadata Filtering**: Extract detector-specific information like type, location, and usability.
- **Visualization**: Generate customizable plots of detector positions with geometry and usability information.


## **Installation**

### Prerequisites
- Python 3.6 or higher
- Access to LEGEND metadata (via `legendmeta` and `lgdo` libraries)
- A Linux-based system (e.g., NERSC environment or LEGEND Shifter container)

### Steps to Install
1. Clone the repository:
   ```bash
   git clone git@github.com:mababicz/legend200-detector-mapper.git
   cd legend200-detector-mapper
