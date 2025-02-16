import pandas as pd

# Define the input FASTA file
fasta_file = "orf_trans_all.fasta"

# Lists to store extracted data
orf_names = []
gene_names = []

# Read and parse the FASTA file
with open(fasta_file, "r") as file:
    for line in file:
        if line.startswith(">"):  # FASTA headers start with ">"
            parts = line.strip().split()  # Split by whitespace
            orf = parts[0][1:]  # Remove ">" from ORF name
            gene = parts[1] if len(parts) > 1 else "Unknown"  # Extract gene name
            orf_names.append(orf)
            gene_names.append(gene)

# Convert to a structured format
df = pd.DataFrame({"ORF Name": orf_names, "Gene Name": gene_names})

# Save to CSV file
output_file = "s288c_gene_names.csv"
df.to_csv(output_file, index=False)

# Print confirmation message
print(f"Extraction complete! Results saved in {output_file}")

# Display first few rows
print(df.head())

