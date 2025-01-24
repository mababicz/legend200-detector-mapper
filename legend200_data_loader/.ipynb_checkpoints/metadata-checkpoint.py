# metadata.py
import os
from legendmeta import LegendMetadata
from legend200_data_loader.logger import setup_logger

class MetadataLoader:
    def __init__(self, ssh_auth_sock=None):
        if ssh_auth_sock:
            os.environ["SSH_AUTH_SOCK"] = ssh_auth_sock
        
        # Setting up the logger
        self.logger = setup_logger()
        
        try:
            # Explicitly set the path for LegendMetadata
            self.lmeta = LegendMetadata(path="/tmp/legend-metadata-mababicz/hardware/configuration/channelmaps")
        except Exception as e:
            self.logger.error(f"Failed to initialize LegendMetadata: {e}")

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

    def filter_metadata(self, detector_type):
        """
        Load Legend Metadata and select only valid_detector_types.
        Also creates a list with all expected rawids of all detector types.
        """
        detectors = {}
        icpc_detectors = []
        ppc_detectors = []
        bege_detectors = []

        try:
            # Loop over legend metadata dictionary
            for key, item in self.lmeta.channelmap().items():
                # Skip non-geds detector systems
                if not item['system'] == 'geds':
                    continue

                detector_dict = {
                    'rawid': item['daq']['rawid'],
                    'type': item['type'],
                    'manufacturer': item['production']['manufacturer'],
                    'processable': item['analysis']['processable'],
                    'lq': item['analysis']['psd']['status']['lq']
                }
                detectors[key] = detector_dict

                # Create lists with rawids based on detector type
                if item['type'] == 'icpc':
                    icpc_detectors.append(item['daq']['rawid'])
                elif item['type'] == 'ppc':
                    ppc_detectors.append(item['daq']['rawid'])
                elif item['type'] == 'bege':
                    bege_detectors.append(item['daq']['rawid'])

            # Fill lists into dictionary
            detectors['rawid_lists'] = {
                'ICPC': icpc_detectors,
                'PPC': ppc_detectors,
                'BEGe': bege_detectors
            }

            # Return the filtered metadata for the requested detector type
            return detectors['rawid_lists'].get(detector_type.upper(), [])

        except Exception as e:
            self.logger.error(f"Failed to filter metadata for detector type {detector_type}: {e}")
            return None
