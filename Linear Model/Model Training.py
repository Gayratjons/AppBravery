import pandas as pd
# # Filtering
df = pd.read_csv("startups_funding_dataset_2024_2025.csv").drop(columns=["Funding Stage", "Country"])
df.to_csv("startup.csv", index=False)