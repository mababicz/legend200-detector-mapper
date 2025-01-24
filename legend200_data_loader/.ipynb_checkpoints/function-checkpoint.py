def filter_metadata(legend_metadata: dict) -> dict:
    """
    Load Legend Metadata and select only valid_detector_types. 
    Also creates a list with all expected rawids of all detector types.

    Parameters:
    legend_metadata    --    instance LegendMetadata which contains LEGEND metadata

    Returns:
    detectors    --    dictionary containing name and id of the expected detectors
    """

    detectors = {}
    icpc_detectors = []
    ppc_detectors = []
    bege_detectors = []

    # Loop over legend metadata dictionary
    for key, item in legend_metadata.channelmap().items():

        # Skip non-geds detector systems
        if not item['system'] == 'geds':
            continue
        detector_dict = {}

        # Add important fields
        detector_dict['rawid'] = item['daq']['rawid']
        detector_dict['type'] = item['type']
        detector_dict['manufacturer'] = item['production']['manufacturer']
        detector_dict['processable'] = item['analysis']['processable']
        detector_dict['lq'] = item['analysis']['psd']['status']['lq']
        detectors[key] = detector_dict

        # Create lists with rawids
        if item['type'] == 'icpc':
            icpc_detectors.append(item['daq']['rawid'])
        elif item['type'] == 'ppc':
            ppc_detectors.append(item['daq']['rawid'])
        elif item['type'] == 'bege':
            bege_detectors.append(item['daq']['rawid'])
        elif item['type'] == 'coax':
            pass # skip for now
        else:
            pass # dont need this

        # Fill lists into dictionary
        detectors['rawid_lists'] = {
            'ICPC': icpc_detectors,
            'PPC': ppc_detectors,
            'BEGe': bege_detectors,
            }

    return detectors
