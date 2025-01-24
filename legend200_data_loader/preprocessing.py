import matplotlib.pyplot as plt
import matplotlib.patches as patches

import os
import re
from lgdo import lh5

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_detector_positions(usable_detectors, legend_metadata, period=None, run=None, ac_detectors=None, off_detectors=None, save_path=None):
    """
    Plot the detector positions as rectangles on a 2D plot using string (X-axis) and position (Y-axis),
    scaled to represent the detector's width (2 * radius) and height (height_in_mm). Detectors are color-coded
    based on their type and usability status.

    Parameters:
    - usable_detectors: List of detector IDs marked as 'on'.
    - legend_metadata: An instance of LegendMetadata to retrieve positions and geometry.
    - period: The data period being plotted (optional).
    - run: The data run being plotted (optional).
    - ac_detectors: List of detector IDs marked as 'ac' (optional).
    - off_detectors: List of detector IDs marked as 'off' (optional).

    Returns:
    - None: Displays a plot of detector positions.
    """
    try:
        # Define color mapping for different detector types
        type_colors = {
            'icpc': 'blue',
            'ppc': 'green',
            'bege': 'red',
            'coax': 'purple'
        }

        # Define usability color overrides
        usability_colors = {
            'on': None,  # Use default type color
            'ac': 'lightgrey',  # Mark 'ac' detectors with light grey
            'off': 'none'  # Mark 'off' detectors with no fill
        }

        # Ensure all inputs are lists or empty lists
        usable_detectors = list(usable_detectors) if usable_detectors else []
        ac_detectors = list(ac_detectors) if ac_detectors else []
        off_detectors = list(off_detectors) if off_detectors else []

        # Combine all detector IDs for plotting
        all_detectors = usable_detectors + ac_detectors + off_detectors

        # Determine the maximum width and height among all detectors
        max_width = 0
        max_height = 0

        # Collect geometry information for scaling calculations
        detector_geometries = []

        for detector_id in all_detectors:
            try:
                detector_info = legend_metadata.channelmap().get(detector_id, None)
                if detector_info:
                    geometry = detector_info.get('geometry', {})
                    height = geometry.get('height_in_mm', 0)
                    radius = geometry.get('radius_in_mm', 0)
                    width = 2 * radius

                    # Store for later use
                    detector_geometries.append((
                        detector_info['location']['string'],
                        detector_info['location']['position'],
                        width,
                        height,
                        detector_info.get('type', '').lower(),
                        detector_id
                    ))

                    # Update max dimensions for scaling
                    if width > max_width:
                        max_width = width
                    if height > max_height:
                        max_height = height
                else:
                    print(f"Metadata for detector {detector_id} not found.")
                    continue

            except KeyError:
                print(f"Error retrieving data for detector {detector_id}.")
                continue

        # Determine scaling factors to fit within the plot (0-12 for x-axis, 15-0 for y-axis)
        x_scale_factor = 0.8 / max_width if max_width > 0 else 1
        y_scale_factor = 0.8 / max_height if max_height > 0 else 1

        # Use the smaller scale factor to keep proportions and avoid overlap
        scale_factor = min(x_scale_factor, y_scale_factor)

        # Set up the plot
        plt.figure(figsize=(14, 12))
        ax = plt.gca()

        # Draw the rectangles
        for string, y_position, width, height, detector_type, detector_id in detector_geometries:
            # Apply scaling
            scaled_width = width * scale_factor
            scaled_height = height * scale_factor

            # Determine usability and corresponding color
            if detector_id in usable_detectors:
                color = type_colors.get(detector_type, 'gray')
                facecolor = color  # Use default color for usable detectors
            elif detector_id in ac_detectors:
                color = usability_colors['ac']  # Light grey for 'ac' detectors
                facecolor = color
            elif detector_id in off_detectors:
                color = usability_colors['off']  # No fill for 'off' detectors
                facecolor = color
            else:
                color = 'gray'  # Default color for any unhandled cases
                facecolor = color

            # Create a rectangle patch aligned at the bottom of the y_position
            rect = patches.Rectangle(
                (string - scaled_width / 2, y_position),  # Bottom-left corner aligned with y_position
                scaled_width, scaled_height,
                edgecolor='black',
                facecolor=facecolor,
                alpha=0.5 if facecolor != 'none' else 1  # Apply transparency only if there is a fill
            )
            ax.add_patch(rect)

            # Annotate with detector ID just below the rectangle's bottom edge
            plt.text(string, y_position - 0.1, detector_id, fontsize=10, ha='center', va='top', color='black')

        # Plot settings
        title = 'Detector Positions'
        if period or run:
            title += f" (Period: {period or 'N/A'}, Run: {run or 'N/A'})"
        plt.title(title, fontsize=16)
        plt.xlabel('String', fontsize=14)
        plt.ylabel('Position', fontsize=14)
        plt.xlim(0, 12)  # Set X-axis from 0 to 12
        plt.ylim(15, 0)  # Set Y-axis from 15 to 0 (inverted)
        plt.grid(True)

        # Set axis ticks to show values at each step
        ax.set_xticks(range(0, 13, 1))  # X-axis ticks from 0 to 12 in steps of 1
        ax.set_yticks(range(0, 16, 1))  # Y-axis ticks from 0 to 15 in steps of 1

        # Add legend
        legend_handles = []
        for dtype, color in type_colors.items():
            legend_handles.append(patches.Patch(color=color, label=dtype.upper(), alpha=0.5))
        
        # Add 'AC' and 'OFF' to legend only if there are corresponding detectors
        if ac_detectors:
            legend_handles.append(patches.Patch(color=usability_colors['ac'], label='AC', alpha=0.5))
        if off_detectors:
            legend_handles.append(patches.Patch(color='black', label='OFF', alpha=1, fill=False))  # Edge-only for 'off'

        plt.legend(handles=legend_handles, title='Detector Types and Usability')
        
        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(save_path, dpi=300)
            print(f"Plot saved to {save_path}")

        plt.show()

    except Exception as e:
        print(f"Error plotting detector positions with geometry: {e}")


import os
import pickle


def load_pickle_file(file_path):
    """
    Loads a pickle file and returns its content.

    Parameters:
    - file_path: str, path to the pickle file to be loaded.

    Returns:
    - data: The loaded data from the pickle file.
    """
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    except Exception as e:
        print(f"Error loading pickle file {file_path}: {e}")
        return None

def extract_detector_info(data, legend_metadata):
    """
    Extracts detector information from the data and metadata.

    Parameters:
    - data: The data containing detector information.
    - legend_metadata: An instance of LegendMetadata to retrieve geometry and usability information.

    Returns:
    - detector_info_list: A list of tuples with (detector_id, string, position, width, height, type, usability).
    """
    detector_info_list = []

    for detector_id in data['channel_id']:
        # Retrieve detector metadata
        try:
            detector_metadata = legend_metadata.channelmap().get(detector_id, None)
            if detector_metadata:
                geometry = detector_metadata.get('geometry', {})
                height = geometry.get('height_in_mm', 0)
                radius = geometry.get('radius_in_mm', 0)
                width = 2 * radius
                det_type = detector_metadata.get('type', 'unknown').lower()
                usability = detector_metadata.get('analysis', {}).get('usability', 'unknown')
                string = detector_metadata['location']['string']
                position = detector_metadata['location']['position']

                detector_info_list.append((detector_id, string, position, width, height, det_type, usability))
            else:
                print(f"Metadata for detector {detector_id} not found.")
        except KeyError as e:
            print(f"Error retrieving metadata for detector {detector_id}: {e}")

    return detector_info_list

def plot_detector_positions_with_data(data_files, legend_metadata, period=None, run=None):
    """
    Loads data from the pickle files, extracts detector information, and plots the detectors.

    Parameters:
    - data_files: List of paths to the pickle files containing detector data.
    - legend_metadata: An instance of LegendMetadata to retrieve positions and geometry.
    - period: Optional period to include in the plot title.
    - run: Optional run to include in the plot title.

    Returns:
    - None: Shows a plot of detector positions.
    """
    # Load data from pickle files
    all_detector_info = []
    for file_path in data_files:
        data = load_pickle_file(file_path)
        if data is not None:
            detector_info_list = extract_detector_info(data, legend_metadata)
            all_detector_info.extend(detector_info_list)

    # Plotting settings
    plt.figure(figsize=(12, 10))
    ax = plt.gca()

    # Define color mapping for detector types and usability
    type_colors = {'icpc': 'blue', 'ppc': 'green', 'bege': 'red'}
    usability_colors = {'on': 'cyan', 'ac': 'yellow', 'off': 'gray'}

    # Plot detector rectangles
    for detector_id, string, position, width, height, det_type, usability in all_detector_info:
        # Get color for type and usability
        color = type_colors.get(det_type, 'gray')
        if usability in usability_colors:
            color = usability_colors[usability]

        # Create a rectangle patch aligned at the bottom of the y_position
        rect = patches.Rectangle(
            (string - width / 2, position),  # Bottom-left corner
            width, height,
            edgecolor='black',
            facecolor=color,
            alpha=0.5
        )
        ax.add_patch(rect)

        # Annotate with detector ID just below the rectangle's bottom edge
        plt.text(string, position - 0.1, detector_id, fontsize=8, ha='center', va='top', color='black')

    # Plot settings
    title = 'Detector Positions with Geometry'
    if period and run:
        title += f' for {period} - {run}'
    plt.title(title)
    plt.xlabel('String')
    plt.ylabel('Position')
    plt.xlim(0, 12)  # Set X-axis from 0 to 12
    plt.ylim(15, 0)  # Set Y-axis from 15 to 0 (inverted)
    plt.grid(True)

    # Set axis ticks
    ax.set_xticks(range(0, 13, 1))
    ax.set_yticks(range(0, 16, 1))

    # Add legend
    for dtype, color in type_colors.items():
        ax.plot([], [], color=color, label=dtype.upper(), linewidth=10, alpha=0.5)
    for usability, color in usability_colors.items():
        ax.plot([], [], color=color, label=f'Usability: {usability}', linewidth=10, alpha=0.5)
    plt.legend(title='Detector Types & Usability')

    plt.show()
