from legend200_data_loader.config import GLOBAL_PARAM

def merge_data():
    merge_params = GLOBAL_PARAM['MERGE']
    periods_to_merge = merge_params['periods_to_merge']
    desired_fields = merge_params['desired_fields']

    # Implement the logic to merge the data from different periods
    # Make sure to extract only the `desired_fields` from each data file
    for period in periods_to_merge:
        # Merge logic here
        pass
