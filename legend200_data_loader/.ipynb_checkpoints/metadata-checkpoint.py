# metadata.py
import os
from legendmeta import LegendMetadata

class MetadataLoader:
    def __init__(self, ssh_auth_sock):
        os.environ["SSH_AUTH_SOCK"] = ssh_auth_sock
        self.lmeta = LegendMetadata()

    def get_channel_id(self, detector_name):
        """
        Retrieve the channel ID for a given detector.
        """
        return self.lmeta.channelmap()[detector_name]['daq']['rawid']
