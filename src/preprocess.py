import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("en-fr.csv")

# Drop rows with missing values
df = df.dropna()

# Filter out sentences that are too long and contain corrupted translations
df = df[df['en'].apply(lambda x: len(str(x)) <= 100)]
df = df[df['fr'].apply(lambda x: len(str(x)) <= 100)]

df = df[~df['fr'].str.contains('Ã')]

# Select a random 50% of the data
random_sample = df.sample(frac=0.5)

# Save the filtered and sampled data to a new CSV file
random_sample.to_csv("filtered_en-fr.csv", index=False)