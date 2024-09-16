# utils.py
#helper functions

import os

def file_exists(file_path):
    """Check if a file exists."""
    return os.path.isfile(file_path)

def list_files(directory, extension=".h5"):
    """List files in a directory with a specific extension."""
    return [f for f in os.listdir(directory) if f.endswith(extension)]
