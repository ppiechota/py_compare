import json
from deepdiff import DeepDiff
from deepdiff_viewer.rich import DeepDiffTreeViewer  # Correct class name
import argparse
from datetime import datetime
from rich.console import Console

def main(file1, file2):
    # Read JSON data from files
    with open(file1, 'r', encoding='utf-8') as f:
        data1 = json.load(f)
    with open(file2, 'r', encoding='utf-8') as f:
        data2 = json.load(f)

    # Calculate differences using DeepDiff
    diff = DeepDiff(data1, data2, view="tree")

    # Generate a timestamped filename for the output
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = f"differences_output_{timestamp}.txt"

    # Initialize the DeepDiffTreeViewer with the diff result
    viewer = DeepDiffTreeViewer(diff)  # Pass the diff directly to the viewer

    # Create a console that writes to a file
    with Console(file=open(output_file, "w"), record=True) as console:
        # Print the rendered diff using the viewer with the console redirected to the file
        console.print(viewer)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare two JSON files and report differences with enhanced visualization.")
    parser.add_argument("file1", type=str, help="The path to the first JSON file.")
    parser.add_argument("file2", type=str, help="The path to the second JSON file.")

    args = parser.parse_args()

    main(args.file1, args.file2)
