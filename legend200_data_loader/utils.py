# utils.py
#helper functions

import os
from legend200_data_loader.logger import setup_logger

logger = setup_logger()

def file_exists(file_path):
    """Check if a file exists."""
    exists = os.path.isfile(file_path)
    logger.info(f"File {'exists' if exists else 'does not exist'}: {file_path}")
    return exists

def list_files(directory, extension=".h5"):
    """List files in a directory with a specific extension."""
    if not os.path.isdir(directory):
        logger.error(f"Directory does not exist: {directory}")
        return []
    
    files = [f for f in os.listdir(directory) if f.endswith(extension)]
    logger.info(f"Files found in {directory}: {files}")
    return files
