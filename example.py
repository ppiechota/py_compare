def format_deepdiff_output(diff):
    output_lines = []
    for key, changes in diff.items():
        if changes:
            output_lines.append(f"{key.capitalize()}:")
            if isinstance(changes, dict):
                for item_path, change_detail in changes.items():
                    if isinstance(change_detail, dict) and 'new_value' in change_detail:
                        output_lines.append(f"  At {item_path}, changed from {change_detail['old_value']} to {change_detail['new_value']}.")
                    else:
                        output_lines.append(f"  At {item_path}, {change_detail}.")
            elif isinstance(changes, list):
                for change in changes:
                    output_lines.append(f"  {change}")
            else:
                output_lines.append(f"  {changes}")
    return "\n".join(output_lines)
