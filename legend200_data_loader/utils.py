# utils.py
# Helper functions

import os
from legend200_data_loader.logger import setup_logger

logger = setup_logger()

def file_exists(file_path):
    """
    Check if a file exists.

    Parameters:
    file_path (str): Path to the file.

    Returns:
    bool: True if the file exists, False otherwise.
    """
    try:
        exists = os.path.isfile(file_path)
        abs_path = os.path.abspath(file_path)
        logger.info(f"File {'exists' if exists else 'does not exist'}: {abs_path}")
        return exists
    except Exception as e:
        logger.error(f"Error checking file existence for {file_path}: {e}")
        return False

def list_files(directory, extension=".h5", log_files=True):
    """
    List files in a directory with a specific extension.

    Parameters:
    directory (str): Path to the directory.
    extension (str): File extension to filter by (default is ".h5").
    log_files (bool): Whether to log the files found (default is True).

    Returns:
    list: List of files with the specified extension in the directory.
    """
    try:
        if not os.path.isdir(directory):
            abs_dir = os.path.abspath(directory)
            logger.error(f"Directory does not exist: {abs_dir}")
            return []

        files = [f for f in os.listdir(directory) if f.endswith(extension)]
        
        if log_files:
            logger.info(f"Files found in {os.path.abspath(directory)}: {files}")
        
        return files
    except Exception as e:
        logger.error(f"Error listing files in directory {directory}: {e}")
        return []
