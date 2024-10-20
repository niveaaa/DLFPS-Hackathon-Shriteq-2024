import pandas as pd

# Load the uploaded file
file_path = "train.tsv"

# Read and display the first few rows
data = pd.read_csv(file_path, sep='\t')
print(data.head())
print(data.columns)

# Extract the relevant columns
X = data.iloc[:, 2].values  # Assuming the third column is the text

# Map truth labels to numeric values (binary)
label_mapping = {
    'false': 0,
    'half-true': 0,  # Consider 'half-true' as fake for binary classification
    'true': 1,
    'mostly-true': 1
}
y = data.iloc[:, 1].map(label_mapping).values  # Assuming the second column has labels

print(X[:5])  # Display first 5 texts
print(y[:5])  # Display first 5 labels
