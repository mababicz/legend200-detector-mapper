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

## IMPORTANT (it is going to work only if you are LEGEND collaborator): Setting Up SSH for Git and Jupyter Integration

To use the tool and access LEGEND metadata (via SSH) on NERSC or similar systems, you need to set up an SSH agent. Follow these steps to set up SSH and use it in Jupyter:

### **1. Generate and Add an SSH Key**
If you don’t already have an SSH key configured, follow the official GitHub instructions: [Generate a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

### **2. Configure Git**
Run the following commands to configure Git and start the SSH agent:
```bash
git config --global user.name "xxxxx"
git config --global user.email "xxx@yyy"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
