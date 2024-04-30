import json
from deepdiff import DeepDiff
import argparse
from datetime import datetime

# def format_deepdiff_output(diff):
#     output_lines = []
#     for key, changes in diff.items():
#         if changes:
#             output_lines.append(f"{key.capitalize()}:")
#             if isinstance(changes, dict):
#                 for item_path, change_detail in changes.items():
#                     if isinstance(change_detail, dict) and 'new_value' in change_detail:
#                         output_lines.append(f"  At {item_path}, changed from {change_detail['old_value']} to {change_detail['new_value']}.")
#                     else:
#                         output_lines.append(f"  At {item_path}, {change_detail}.")
#             elif isinstance(changes, list):
#                 for change in changes:
#                     output_lines.append(f"  {change}")
#             else:
#                 output_lines.append(f"  {changes}")
#     return "\n".join(output_lines)

def format_deepdiff_output(diff):
    output_lines = []
    for key, changes in diff.items():
        if changes:
            output_lines.append(f"{key.capitalize()}:")
            if isinstance(changes, dict):
                for item_path, change_detail in changes.items():
                    # Apply indentation based on depth
                    depth = item_path.count('[')
                    indent = '    ' * depth  # Using four spaces for each level of indentation
                    if isinstance(change_detail, dict) and 'new_value' in change_detail:
                        output_lines.append(f"{indent}At {item_path}, changed from {change_detail['old_value']} to {change_detail['new_value']}.")
                    else:
                        output_lines.append(f"{indent}At {item_path}, {change_detail}.")
            elif isinstance(changes, list):
                for item in changes:
                    # This assumes the list items are strings describing the changes
                    depth = item.count('[')
                    indent = '    ' * depth  # Using four spaces for each level of indentation
                    output_lines.append(f"{indent}{item}")
            else:
                # Handle non-list, non-dict types conservatively
                output_lines.append(f"  {changes}")
    return "\n".join(output_lines)



def main(file1, file2):
    # Read JSON data from files
    with open(file1, 'r', encoding='utf-8') as f:
        data1 = json.load(f)

    with open(file2, 'r', encoding='utf-8') as f:
        data2 = json.load(f)

    # Generate a timestamped filename for the output
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = f"differences_output_{timestamp}.txt"

    # Calculate differences
    diff = DeepDiff(data1, data2, ignore_order=True)

    # Format the output
    formatted_output = format_deepdiff_output(diff)
    
    # Save the formatted output to a text file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(formatted_output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare two JSON files and report differences.")
    parser.add_argument("file1", type=str, help="The path to the first JSON file.")
    parser.add_argument("file2", type=str, help="The path to the second JSON file.")

    args = parser.parse_args()

    main(args.file1, args.file2)
