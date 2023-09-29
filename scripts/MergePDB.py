import argparse
import pandas as pd

def concatenate_all(series):
    return '\n'.join(series.astype(str))

def concatenate_unique(series):
    return '\n'.join(map(str, series.unique()))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Concatenate rows with the same sequence and sort by PDB.')
    parser.add_argument('input', type=str, help='Path to the input CSV file containing protein sequence data.')
    parser.add_argument('output', type=str, help='Path to write the output CSV file containing processed and sorted protein sequence data.')
    args = parser.parse_args()

    input_path = args.input
    output_path = args.output

    data = pd.read_csv(input_path)
    
    # Group by 'Sequence' and concatenate the rows with the appropriate function
    grouped_data = data.groupby('Sequence').agg({
        'PDB': concatenate_all,
        'Method': concatenate_all,
        'Resolution': concatenate_all,
        'Secondary Structure Type': concatenate_unique,
        'Positions': concatenate_all,
        'Lenght': concatenate_unique
    }).reset_index()

    # Sort by 'PDB' and write to the output file
    grouped_data.sort_values(by='PDB').to_csv(output_path, index=False)