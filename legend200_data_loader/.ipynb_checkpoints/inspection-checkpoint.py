from lgdo.lh5 import load_datasets, load_nda
import os

def inspect_raw_data_file(file_dict, tier='raw_files'):
    """
    Inspects the contents of a raw .lh5 data file.

    Parameters:
    - file_dict: Dictionary of files from the data loader.
    - tier: The tier to check (default is 'raw_files').

    Returns:
    - None: Prints the structure of the file.
    """
    # Check if the specified tier has files
    if tier in file_dict and file_dict[tier]:
        raw_file_path = file_dict[tier][0]  # Get the first file from the specified tier
        print(f"Inspecting raw file: {os.path.basename(raw_file_path)}")
        
        try:
            # Use load_datasets to find available datasets in the file
            datasets = load_datasets(raw_file_path)
            print("Datasets available in the file:")
            for ds_name in datasets:
                print(f" - {ds_name}")

            # Choose the first dataset for demonstration purposes
            par_list = list(datasets.keys())

            # Load data using the par_list
            data, n_rows = load_nda(raw_file_path, par_list=par_list)
            
            # Display the first dataset details
            first_key = par_list[0]
            dataset = data[first_key]
            print(f"\nDetails of the first dataset ({first_key}):")
            print(f"Type: {type(dataset)}")
            print(f"Shape: {dataset.shape}")
            if hasattr(dataset, 'metadata'):
                print(f"Metadata: {dataset.metadata}")
                
        except Exception as e:
            print(f"Error inspecting raw data file: {e}")
    else:
        print(f"No files found in tier: {tier}.")
