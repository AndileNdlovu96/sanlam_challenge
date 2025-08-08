import pandas as pd

def clean_data(csv_path):
    df = pd.read_csv(csv_path)

    # Drop rows with no names
    df = df.dropna(subset=["FullName"])

    # Fill blanks
    df["Comments"] = df["Comments"].fillna("No comments")
    df["IndividualAlias"] = df["IndividualAlias"].fillna("")

    # Strip whitespace
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    # Optional: Normalize names to uppercase
    df["FullName"] = df["FullName"].str.upper()

    df.to_parquet("output/sanctions_cleaned.parquet", index=False)
    print("Saved cleaned data to output/sanctions_cleaned.parquet")

if __name__ == "__main__":
    clean_data("output/raw_sanctions.csv")
