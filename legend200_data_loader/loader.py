# loader.py

#this is to handle loading HDF5 files, manage the data tiers"
#raw, dsp, pht, pet, skm and integrate metadata from SSH connections

#created by M. Babicz 

import os
import h5py
from legendmeta import LegendMetadata
from lgdo import lh5
from legend200_data_loader.config import GLOBAL_PARAM
from legend200_data_loader.logger import setup_logger

class LegendDataLoader:
    def __init__(self):
        # Set up the logger
        self.logger = setup_logger()
        # Load global parameters
        self.data_dir = GLOBAL_PARAM['DIRS']['LEGEND_DATA_DIR']
        self.raw_subdir = GLOBAL_PARAM['DIRS']['RAW_SUBDIR']
        self.pht_subdir = GLOBAL_PARAM['DIRS']['PHT_SUBDIR']
        self.tcm_subdir = GLOBAL_PARAM['DIRS']['TCM_SUBDIR']
        self.periods = GLOBAL_PARAM['DIRS']['PERIODS']

    def load_raw_data(self):
        """
        Load raw data files from the specified periods.
        """
        loaded_data = {}
        for period in self.periods:
            raw_path = os.path.join(self.data_dir, self.raw_subdir, period)
            self.logger.info(f"Loading raw data from {raw_path}")
            if not os.path.exists(raw_path):
                self.logger.error(f"Path does not exist: {raw_path}")
                continue
            
            files = [f for f in os.listdir(raw_path) if f.endswith('.h5')]
            for file in files:
                file_path = os.path.join(raw_path, file)
                with h5py.File(file_path, 'r') as f:
                    loaded_data[file] = f  # Example: you may want to parse this into a usable format
                self.logger.info(f"Loaded file: {file_path}")
        
        return loaded_data

    # Similar methods for loading other data tiers (PHT, TCM, etc.) can be added here

    def load_metadata(self):
        """
        Example metadata loading using LegendMetadata.
        """
        lmeta = LegendMetadata()
        # Implement metadata loading as required
        return lmeta

