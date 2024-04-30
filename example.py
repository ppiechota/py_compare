import json
from deepdiff import DeepDiff
from deepdiff_viewer.rich import RichViewer  # Importing the RichViewer
import argparse
from datetime import datetime

def main(file1, file2):
    # Read JSON data from files
    with open(file1, 'r', encoding='utf-8') as f:
        data1 = json.load(f)
    with open(file2, 'r', encoding='utf-8') as f:
        data2 = json.load(f)

    # Calculate differences using DeepDiff
    diff = DeepDiff(data1, data2, view="tree")

    # Create a RichViewer instance
    viewer = RichViewer()

    # Print the diff using the RichViewer
    viewer.pprint(diff)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare two JSON files and report differences with enhanced visualization.")
    parser.add_argument("file1", type=str, help="The path to the first JSON file.")
    parser.add_argument("file2", type=str, help="The path to the second JSON file.")

    args = parser.parse_args()

    main(args.file1, args.file2)
