# metadata.py
import os
from legendmeta import LegendMetadata
from legend200_data_loader.logger import setup_logger

class MetadataLoader:
    def __init__(self, ssh_auth_sock=None):
        if ssh_auth_sock:
            os.environ["SSH_AUTH_SOCK"] = ssh_auth_sock
        self.logger = setup_logger()
        self.lmeta = LegendMetadata()

    def get_channel_id(self, detector_name):
        """
        Retrieve the channel ID for a given detector.
        """
        try:
            channel_id = self.lmeta.channelmap()[detector_name]['daq']['rawid']
            self.logger.info(f"Channel ID for {detector_name}: {channel_id}")
            return channel_id
        except KeyError:
            self.logger.error(f"Detector {detector_name} not found in metadata.")
            return None
