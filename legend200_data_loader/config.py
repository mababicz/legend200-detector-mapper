# config.py

GLOBAL_PARAM = {
    'DIRS': { 
        'LEGEND_DATA_DIR': '/dvs_ro/cfs/cdirs/m2676/data/lngs/l200/public/prodenv/prod-blind/',
        'TYPE': 'cal/',
        'RAW_SUBDIR': 'ref-raw/generated/tier/raw/',  # waveforms
        'PHT_SUBDIR': 'ref-v2.0.0/generated/tier/pht/',  # higher-level attributes
        'TCM_SUBDIR': 'ref-v2.0.0/generated/tier/tcm/',  # pulser events
        'PSP_SUBDIR': 'ref-v2.0.0/generated/tier/psp/',  # DCR param -> Not yet used
        'PAR_SUBDIR': 'ref-v2.0.0/generated/par/pht/',  # Ecal parameters
        'PERIODS': ['p03/', 'p08/', 'p09/', 'p10/'],
        'output_dir': '/pscratch/sd/m/mababicz/DATA/'
    },
    'peaks': {
        'DEP_Tl': 1592.53,
        'FEP_Bi': 1620.5,
        'SEP_Tl': 2103.53,
        'FEP_Tl': 2614.553
    },
    'auto_peak_selection': True,  # NOTE: manual peak selection not implemented yet
    'cut_value_sigmas': 3,
    'detector_type': 'ICPC',
    'valid_detector_types': ['ICPC', 'BEGe', 'PPC'],
    'inactive_detectors': [],  # Example: ['V01403A', 'V07298B', 'V01404A'],
    'exclude_period_run': ['p08_r005'],
    'MERGE': {
        'periods_to_merge': ['p03/', 'p06/', 'p07/', 'p08/', 'p09/'],
        'replace_files': True,
        'desired_fields': [
            'timestamp', 'tp_0_est', 'dt_eff', 'zacEmax_cal', 'cuspEmax_ctc_cal',
            'AoE_High_Side_Cut', 'AoE_Low_Cut', 'AoE_Double_Sided_Cut',
            'LQ_Cut', 'bl_pileup_cut_classifier', 'bl_pileup_cut', 'tail_pileup_cut_classifier',
            'tail_pileup_cut', 'is_surface', 'waveform', 'channel_id', 'peak'
        ],
    }
}
