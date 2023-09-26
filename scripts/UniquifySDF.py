import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse SDF file and check for unique sequences.')
    parser.add_argument('sdf_file_path', type=str, help='Path to the SDF file.')
    parser.add_argument('unique_sdf_file_path', type=str, help='Path to the output folder.')
    args = parser.parse_args()

    sdf_file_path = args.sdf_file_path
    unique_sdf_file_path = args.unique_sdf_file_path

    try:
        with open(sdf_file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File {sdf_file_path} not found.")
        exit(1)

    entries = content.split('$$$$\n')

    unique_entries = {}

    for entry in entries:
        lines = entry.split('\n')
        if lines:
            sequence = lines[0].strip()
            if sequence and sequence not in unique_entries:
                unique_entries[sequence] = entry

    with open(unique_sdf_file_path, 'w', encoding='utf-8') as file:
        for entry in unique_entries.values():
            file.write(entry)
            file.write('$$$$\n')

    print(f"Unique entries are written to {unique_sdf_file_path}")