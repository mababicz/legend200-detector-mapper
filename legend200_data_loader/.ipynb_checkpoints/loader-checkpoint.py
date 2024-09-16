# loader.py

#this is to handle loading HDF5 files, manage the data tiers"
#raw, dsp, pht, pet, skm and integrate metadata from SSH connections

#created by M. Babicz 

import h5py
from legendmeta import LegendMetadata
import logging
from lgdo import lh5
from legend200_data_loader.config import DATA_PATH

class LegendDataLoader:
    def __init__(self, lh5_files, tier='pet'):
        """
        Initialize the data loader with file paths and tier to be loaded.
        """
        self.lh5_files = lh5_files
        self.tier = tier
        self.metadata = None
        logging.info(f"Initialized loader with tier: {self.tier}")

    def load_metadata(self, ssh_auth_sock):
        """
        Load LEGEND-200 metadata via SSH.
        """
        os.environ["SSH_AUTH_SOCK"] = ssh_auth_sock
        self.metadata = LegendMetadata()
        logging.info("Metadata successfully loaded.")
    
    def load_tier_data(self, channel_id):
        """
        Load data from the specific tier.
        """
        try:
            data = lh5.read_as(
                name=f'ch{channel_id}/evt',
                lh5_file=self.lh5_files,
                library="ak"
            )
            logging.info(f"Data loaded for channel: {channel_id}")
            return data
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            raise

    def inspect_file(self):
        """
        Inspect the structure of the HDF5 file.
        """
        lh5.tools.show(self.lh5_files[0])
