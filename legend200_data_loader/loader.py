# loader.py

# This is to handle loading HDF5 files, manage the data tiers (raw, dsp, pht, pet, skm) and integrate metadata from SSH connections.

# Created by M. Babicz 

import os
import h5py
from legendmeta import LegendMetadata
from lgdo import lh5
from legend200_data_loader.config import GLOBAL_PARAM
from legend200_data_loader.logger import setup_logger

import glob
import json

import traceback


class LegendDataLoader:
    def __init__(self):
        self.logger = setup_logger() #o keep track of events and errors
        self.type = GLOBAL_PARAM['DIRS']['TYPE']
        self.data_dir = GLOBAL_PARAM['DIRS']['LEGEND_DATA_DIR']
        self.raw_subdir = GLOBAL_PARAM['DIRS']['RAW_SUBDIR']
        self.pht_subdir = GLOBAL_PARAM['DIRS']['PHT_SUBDIR']
        self.tcm_subdir = GLOBAL_PARAM['DIRS']['TCM_SUBDIR']
        self.psp_subdir = GLOBAL_PARAM['DIRS']['PSP_SUBDIR']
        self.par_subdir = GLOBAL_PARAM['DIRS']['PAR_SUBDIR']
        self.periods = GLOBAL_PARAM['DIRS']['PERIODS']

    def get_runs(self, period):
        """Retrieve run directories for a given period."""
        period_path = os.path.join(self.data_dir, self.raw_subdir, self.type, period)
        try:
            return sorted(os.listdir(period_path))
        except FileNotFoundError:
            self.logger.error(f"Period path not found: {period_path}")
            return []

    def load_files(self, period, run):
        """Load raw, PHT, TCM, PSP, and PAR files for a given period and run.
        Collects and returns a dictionary (file_dict) that contains the paths 
        to each type of file.
        """
        file_dict = {}
        run_path = os.path.join(period, run)
        file_types = {
            'raw_files': os.path.join(self.raw_subdir, self.type, run_path, '*.lh5'),
            'pht_files': os.path.join(self.pht_subdir, self.type, run_path, '*.lh5'),
            'tcm_files': os.path.join(self.tcm_subdir, self.type, run_path, '*.lh5'),
            'psp_files': os.path.join(self.psp_subdir, self.type, run_path, '*.lh5'),
            'par_file': os.path.join(self.par_subdir, self.type, run_path, '*.json')
        }

        for key, pattern in file_types.items():
            files = glob.glob(os.path.join(self.data_dir, pattern))
            if key == 'par_file':  # Only expect one JSON file
                if len(files) != 1:
                    self.logger.error(f"Invalid number of PAR files for {run_path}. Expected 1, found {len(files)}.")
                    continue
                file_dict[key] = files[0]
            else:
                if not files:
                    self.logger.error(f"Missing {key} for {run_path}.")
                else:
                    file_dict[key] = sorted(files)

        return file_dict

    def load_par_file(self, par_file_path):
        """Load a PAR JSON file."""
        try:
            with open(par_file_path, 'r') as par_file:
                return json.load(par_file)
        except Exception as e:
            self.logger.error(f"Failed to load PAR file: {par_file_path}. Error: {e}")
            return None


#class LegendDataLoader:
#    def __init__(self):
        # Set up the logger
#        self.logger = setup_logger()
        
        # Load global parameters
#        self.type = GLOBAL_PARAM['DIRS']['TYPE']
#        self.data_dir = GLOBAL_PARAM['DIRS']['LEGEND_DATA_DIR']
#        self.raw_subdir = GLOBAL_PARAM['DIRS']['RAW_SUBDIR']
#        self.pht_subdir = GLOBAL_PARAM['DIRS']['PHT_SUBDIR']
#        self.tcm_subdir = GLOBAL_PARAM['DIRS']['TCM_SUBDIR']
#        self.psp_subdir = GLOBAL_PARAM['DIRS']['PSP_SUBDIR']
#        self.par_subdir = GLOBAL_PARAM['DIRS']['PAR_SUBDIR']
#        self.periods = GLOBAL_PARAM['DIRS']['PERIODS']

#    def load_raw_data(self):
#        """
#        Load raw data files from the specified periods within the 'cal/' subdirectory.
#        """
#        loaded_data = {}
#        for period in self.periods:
#            raw_path = os.path.join(self.data_dir, self.raw_subdir, self.type, period)
#            self.logger.info(f"Loading raw data from {raw_path}")
#
#            # Check if path exists
#            if not os.path.exists(raw_path):
#                self.logger.error(f"Path does not exist: {raw_path}")
#                continue

            # List .h5 files
#            files = [f for f in os.listdir(raw_path) if f.endswith('.h5')]
            
            # Handle empty directories
#            if not files:
#                self.logger.warning(f"No .h5 files found in {raw_path}")
#                continue

#            self.logger.info(f"Found {len(files)} .h5 files in {raw_path}")

#            for file in files:
#                file_path = os.path.join(raw_path, file)
#                try:
#                    with h5py.File(file_path, 'r') as f:
                        # Example: you may want to parse this into a usable format
#                        loaded_data[file] = f 
#                    self.logger.info(f"Loaded file: {file_path}")
#                except Exception as e:
                    # Handle file read errors
#                    self.logger.error(f"Error loading file {file_path}: {e}")

#        return loaded_data

    

#    def load_metadata(self):
#        """
#        Example metadata loading using LegendMetadata.
#        """
#        lmeta = LegendMetadata()
        # Implement metadata loading as required
#        return lmeta
