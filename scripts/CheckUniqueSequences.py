import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse SDF file and check for unique sequences.')
    parser.add_argument('sdf_file_path', type=str, help='Path to the SDF file.')
    args = parser.parse_args()

    sdf_file_path = args.sdf_file_path

    try:
        with open(sdf_file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File {sdf_file_path} not found.")
        exit(1)

    entries = content.split('$$$$\n')

    sequences = []

    for entry in entries:
        lines = entry.strip().split('\n')
        if lines:
            sequences.append(lines[0].strip())

    sequence_set = set()
    non_unique_sequences = set()

    for sequence in sequences:
        if sequence in sequence_set:
            non_unique_sequences.add(sequence)
        else:
            sequence_set.add(sequence)

    if non_unique_sequences:
        print("The following sequences are not unique:")
        for sequence in non_unique_sequences:
            print(sequence)
        print(f"SDF contains {len(sequences)} sequences")
    else:
        print(f"All sequences are unique. SDF contains {len(sequences)} sequences")