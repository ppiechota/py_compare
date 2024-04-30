import json
from deepdiff import DeepDiff
from deepdiff_viewer import DeepDiffTreeViewer  # Adjusted import for clarity, ensure it's correct as per actual package
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

    # Initialize the viewer with the diff
    viewer = DeepDiffTreeViewer(diff)

    # Generate a timestamped filename for the output
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = f"differences_output_{timestamp}.txt"

    # Using Rich Console to print to a file
    with Console(file=open(output_file, "w"), record=True) as console:
        # Render the diff using the viewer and print it
        rendered_diff = viewer.render()  # Assuming render returns a Rich renderable
        console.print(rendered_diff)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare two JSON files and report differences.")
    parser.add_argument("file1", type=str, help="The path to the first JSON file.")
    parser.add_argument("file2", type=str, help="The path to the second JSON file.")

    args = parser.parse_args()

    main(args.file1, args.file2)
